import datetime
from typing import List, Optional

from pydantic import BaseModel


class PredictionRequest(BaseModel):
    store_id: str
    product_name: List[str]
    date: datetime.datetime
