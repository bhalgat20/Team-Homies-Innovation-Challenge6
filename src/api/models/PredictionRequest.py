import datetime
from typing import List, Optional

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    store_id: str
    products: List[str]
    date: datetime.datetime
