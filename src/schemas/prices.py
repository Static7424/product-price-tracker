from datetime import datetime
from pydantic import BaseModel


class PriceRecordResponse(BaseModel):
    id: int
    product_id: str
    product_price: float
    recorded_at: datetime

    model_config = {"from_attributes": True}
