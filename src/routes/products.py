from fastapi import APIRouter, Depends, Form, HTTPException, Path
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.price import Price
from src.models.product import (
    Product,
    ProductHistoryResponse,
    ProductRegisterResponse,
    ProductResponse,
)


router = APIRouter(prefix="/products", tags=["products"])


@router.post(
    "/register",
    response_model=ProductRegisterResponse,
    status_code=201,
    summary="Register a new product to the PostGres DB.",
)
def register_product(
    product_id: str = Form(..., description="Product ID to register."),
    product_name: str = Form(..., description="Product name to register."),
    product_url: str = Form(..., description="URL to the product to register."),
    db: Session = Depends(get_db),
):
    product = Product(
        product_id=product_id, product_name=product_name, product_url=product_url
    )

    try:
        db.add(product)
        db.commit()
        db.refresh(product)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409, detail="Product with this ID already exists."
        )

    return product


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Get a registered product for a particular product ID.",
)
def product_id(
    product_id: str = Path(..., description="Product ID to get."),
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")

    return product


@router.get(
    "/{product_id}/history",
    response_model=ProductHistoryResponse,
    summary="Get the historic prices for a particular product ID.",
)
def product_id_history(
    product_id: str = Path(..., description="Product ID to get historic prices for."),
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")

    product_prices = (
        db.query(Price)
        .filter(Price.product_id == product_id)
        .order_by(Price.recorded_at)
        .all()
    )

    return ProductHistoryResponse(
        id=product.id, product_id=product.product_id, product_prices=product_prices
    )
