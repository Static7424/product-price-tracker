from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Path
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.price import Price
from src.models.product import Product
from src.schemas.prices import PriceHistoryResponse, PriceRecordResponse

router = APIRouter(prefix="/prices", tags=["prices"])


@router.post(
    "/record",
    response_model=PriceRecordResponse,
    status_code=201,
    summary="Record a price for a product_id in the PostGres DB.",
)
def record_price(
    product_id: Annotated[
        str,
        Form(..., description="Product ID to record the price for.", max_length=100),
    ],
    product_price: Annotated[
        Decimal,
        Form(
            ...,
            description="Product price to record.",
            decimal_places=2,
            gt=0,
            max_digits=10,
        ),
    ],
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
            detail=f"Product ID '{product_id}' has not been registered. Please register it with `/products/register`.",
        )

    return price


@router.get(
    "/{product_id}/history",
    response_model=PriceHistoryResponse,
    summary="Get the historic prices for a particular product ID.",
)
def price_history(
    product_id: Annotated[
        str,
        Path(..., description="Product ID to get historic prices for.", max_length=100),
    ],
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product ID '{product_id}' has not been registered. Please register it with `/products/register`.",
        )

    product_prices = (
        db.query(Price)
        .filter(Price.product_id == product_id)
        .order_by(Price.recorded_at)
        .all()
    )

    return PriceHistoryResponse(
        id=product.id, product_id=product.product_id, product_prices=product_prices
    )
