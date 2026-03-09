from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.price import Price
from src.schemas.prices import PriceRecordResponse


router = APIRouter(prefix="/prices", tags=["prices"])


@router.post(
    "/record",
    response_model=PriceRecordResponse,
    status_code=201,
    summary="Record a price for a product_id in the PostGres DB.",
)
def register_product(
    product_id: str = Form(..., description="Product ID to record the price for."),
    product_price: float = Form(..., description="Product price to record."),
    db: Session = Depends(get_db),
):
    price = Price(product_id=product_id, product_price=product_price)

    try:
        db.add(price)
        db.commit()
        db.refresh(price)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=404,
            detail="Product ID has not been registered. Please register it with '/products/register'.",
        )

    return price
