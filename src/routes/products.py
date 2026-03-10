from fastapi import APIRouter, Form, HTTPException, Path
from sqlalchemy.exc import IntegrityError
from typing import Annotated

from src.database.database import DBSession
from src.models.product import Product
from src.schemas.products import (
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
    product_id: Annotated[
        str,
        Form(..., description="Product ID to register", max_length=100),
    ],
    product_name: Annotated[
        str,
        Form(..., description="Product name to register.", max_length=100),
    ],
    product_url: Annotated[
        str,
        Form(..., description="URL to the product to register."),
    ],
    db: DBSession,
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
            status_code=409, detail=f"Product ID '{product_id}' already exists."
        )

    return product


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Get a registered product for a particular product ID.",
)
def product_id(
    product_id: Annotated[
        str,
        Path(..., description="Product ID to get.", max_length=100),
    ],
    db: DBSession,
):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product ID '{product_id}' has not been registered. Please register it with `/products/register`.",
        )

    return product
