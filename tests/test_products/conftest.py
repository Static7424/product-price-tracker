import pytest


TEST_POST_REGISTER_PRODUCTS_INPUT = [
    {
        "name": "register_single_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            }
        ]
    },
    {
        "name": "register_single_existing_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 409,
                "response_message": "Product ID '1' already exists."
            }
        ]
    },
    {
        "name": "register_single_invalid_product_id",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
                "response_code": 422
            }
        ]
    },
    {
        "name": "register_single_invalid_product_name",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
                "product_url": "https://example.com/product/1",
                "response_code": 422
            }
        ]
    }
]

@pytest.fixture(params = TEST_POST_REGISTER_PRODUCTS_INPUT, ids = lambda x: x["name"])
def test_post_register_products_input(request):
    return request.param


TEST_GET_PRODUCT_INPUT = [
    {
        "name": "get_single_registered_product",
        "product_id": "1",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            }
        ],
        "response_data": {
            "product_id": "1",
            "product_name": "Test Product",
            "product_url": "https://example.com/product/1",
            "response_code": 200
        }
    },
    {
        "name": "get_single_unregistered_product",
        "product_id": "1",
        "queries": [],
        "response_data": {
            "response_code": 404,
            "response_message": "Product ID '1' has not been registered. Please register it with `/products/register`."
        }
    },
    {
        "name": "get_single_invalid_product_name",
        "product_id": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
        "queries": [],
        "response_data": {
            "response_code": 422
        }
    }
]

@pytest.fixture(params = TEST_GET_PRODUCT_INPUT, ids = lambda x: x["name"])
def test_get_product_input(request):
    return request.param
