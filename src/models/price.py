from pydantic import BaseModel
from datetime import datetime

from src.database.database import Reflected


class Price(Reflected):
    __tablename__ = "prices"


class PriceRecordResponse(BaseModel):
    id: int
    product_id: str
    product_price: float
    recorded_at: datetime

    model_config = {
        "from_attributes": True
    }
