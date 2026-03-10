from pydantic import BaseModel


class ProductRegisterResponse(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_url: str

    model_config = {"from_attributes": True}


class ProductResponse(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_url: str

    model_config = {"from_attributes": True}
