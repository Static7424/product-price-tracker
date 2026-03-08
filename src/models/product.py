from pydantic import BaseModel

from src.database.database import Reflected
from src.models.price import PriceRecordResponse


class Product(Reflected):
    __tablename__ = "products"


class ProductRegisterResponse(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_url: str

    model_config = {
        "from_attributes": True
    }


class ProductHistoryResponse(BaseModel):
    id: int
    product_id: str
    product_prices: list[PriceRecordResponse]

    model_config = {
        "from_attributes": True
    }


class ProductResponse(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_url: str

    model_config = {
        "from_attributes": True
    }
