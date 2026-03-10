from datetime import datetime
from pydantic import BaseModel


class PriceEntry(BaseModel):
    id: int
    product_price: float
    recorded_at: datetime

    model_config = {"from_attributes": True}


class PriceHistoryResponse(BaseModel):
    id: int
    product_id: str
    product_prices: list[PriceEntry]

    model_config = {"from_attributes": True}


class PriceRecordResponse(BaseModel):
    id: int
    product_id: str
    product_price: float
    recorded_at: datetime

    model_config = {"from_attributes": True}
