from fastapi import FastAPI
from pydantic import BaseModel
from utils import utils
from data_providers import location_provider, health_status_provider, economy_status_provider, population_density_provider, festivals_provider, weather_data_provider, lot_size_provider


from models.PredictionRequest import PredictionRequest


class DummyRequest(BaseModel):
    num1: float
    num2: float
    num3: float


app = FastAPI()


@app.get('/')
def root():
    return 'Hello There!! Welcome to Smart Invetory'


@app.get('/prediction', status_code=200, response_description="Returns the lot Prediction for the Given Products List",
         )
async def predict(prediction_request: PredictionRequest):
    response = []
    products = prediction_request.products
    for product in products:
        response.append(get_prediction_for_product(prediction_request,product))
    return response


def get_prediction_for_product(prediction_request,product_name):
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
    # TODO: Call Prediction
    final_prediction_val = lot_size_provider.get_lot_size(10, product_name)
    if "None" not in final_prediction_val.split():
        return {f"{product_name}": {
            "location": location,
            "month": month,
            "year": year,
            "economy_status": economy_status,
            "health_status": health_status,
            "population_density": population_density,
            "festivals": festivals,
            "weather": weather,
            "prediction": final_prediction_val
        }}
    else:
        return{
            f"{product_name}":{
                "error":"No Product with the given Name"
            }
        }