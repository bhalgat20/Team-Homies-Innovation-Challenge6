from typing import Dict

from pydantic import BaseModel


class Prediction(BaseModel):
    product_name: str
    quantity: float


class PredictionResponse(BaseModel):
    __root__: Dict[str, Prediction]
