from fastapi import FastAPI
from pydantic import BaseModel
from utils import utils
from data_providers import location_provider,health_status_provider,economy_status_provider,population_density_provider


from models.PredictionRequest import PredictionRequest


class DummyRequest(BaseModel):
    num1: float
    num2: float
    num3: float


app = FastAPI()


@app.get('/')
def root():
    return 'Hello There!! Welcome to FastApi'


@app.get('/prediction', status_code=200, response_description="Returns the lot Prediction for the Given Products List",
         )
async def predict(prediction_request: PredictionRequest):
    store_id = prediction_request.store_id
    product_name = prediction_request.product_name
    month = utils.get_month(prediction_request.date)
    year = utils.get_year(prediction_request.date)
    location = location_provider.get_location(store_id)
    economy_status = economy_status_provider.get_economy_status(location,month,year)
    health_status = health_status_provider.get_health_status(location,month,year)
    population_density = population_density_provider.get_population_density(location)
    return {"prediction_1": {
        "location": location,
        "month": month,
        "year": year,
        "economy_status": economy_status,
        "health_status": health_status,
        "population_density":population_density
    }}
