import os
import pickle
import csv

import pandas as pd
from fastapi import FastAPI

from src.api.data_providers import location_provider, health_status_provider, economy_status_provider, \
    population_density_provider, festivals_provider, weather_data_provider, lot_size_provider, product_category_provider
from src.api.models.PredictionRequest import PredictionRequest
from src.api.models.PredictionResponse import PredictionResponse
from src.api.models.TrainDataRequest import TrainDataRequest
from src.api.utils import utils

INDIA_POPULATION = 1300000000

app = FastAPI()


@app.get('/')
def root():
    return 'Hello There!! Welcome to Smart Invetory'


@app.get('/prediction', status_code=200, response_description="Returns the lot Prediction for the Given Products List",
         response_model=PredictionResponse)
async def predict(prediction_request: PredictionRequest):
    response = []
    products = prediction_request.products
    for product in products:
        response.append(get_prediction_for_product(prediction_request, product))
    return response


@app.post('/update-train-data', status_code=201)
async def update_train_data(train_data: TrainDataRequest):
    with open('./master_data/master_data.csv', 'a') as f:
        for row in train_data.data:
            writer = csv.writer(f)
            writer.writerow(row.dict().values())
    return "Done"


def get_prediction_for_product(prediction_request, product_name):
    store_id = prediction_request.store_id
    month = utils.get_month(prediction_request.date)
    year = utils.get_year(prediction_request.date)
    location = location_provider.get_location(store_id)
    economy_status = economy_status_provider.get_economy_status(
        location, month, year)
    health_status = health_status_provider.get_health_status(
        location, month, year)
    population_density = population_density_provider.get_population_density(
        location)
    festivals = festivals_provider.get_festivals(location, month, year)
    weather = weather_data_provider.get_weather(month)
    product_category = product_category_provider.get_product_category(product_name)
    predicted_lot_size = predict_quantity({
        "store_id": store_id,
        "product_name": product_name,
        "product_category": product_category,
        "month": month,
        "year": year,
        "economy_status": economy_status,
        "health_status": health_status,
        "population_density": population_density,
        "festivals": festivals,
        "weather": weather
    })
    final_prediction_val = lot_size_provider.get_lot_size(predicted_lot_size, product_name)
    if "None" not in final_prediction_val.split():
        return {f"{product_name}": {
            "store_id": prediction_request.store_id,
            "product_name": product_name,
            "prediction": final_prediction_val
        }}
    else:
        return {
            f"{product_name}": {
                "store_id": store_id,
                "product_name": product_name,
                "prediction": "NaN",
                "error": "No Product with the given Name"
            }
        }


def encode_features(store_id):
    encoder_file = open(os.path.join("feature_encoder", f"ohe_{store_id}.obj"), 'rb')
    encoder_loaded = pickle.load(encoder_file)
    encoder_file.close()
    return encoder_loaded


def create_encoded_data_point(data_point, store_id):
    encoder = encode_features(store_id)
    data_point_ohe = encoder.transform(data_point.drop(columns=["population density"], axis=1))
    input_data_point = pd.concat([data_point_ohe, data_point["population density"] / INDIA_POPULATION], axis=1)
    return input_data_point


def predict_quantity(request_details):
    data_point = pd.DataFrame({
        "product name": [request_details['product_name']],
        'p _ category': [request_details['product_category']],
        'eonomical crisis': [request_details['economy_status']],
        'health crisis': [request_details['health_status']],
        'festivals in region ': [request_details['festivals']],
        'weather': [request_details['weather']],
        'population density': [request_details['population_density']]
    })
    input_data_point = create_encoded_data_point(data_point, request_details['store_id'])
    model_file = open(os.path.join("trained_models", f"{request_details['store_id']}.pkl"), 'rb')
    model = pickle.load(model_file)
    predicted_lot_size = model.predict(input_data_point)
    model_file.close()
    return round(predicted_lot_size[0], 1)
