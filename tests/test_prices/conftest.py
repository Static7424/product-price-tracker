import pytest


TEST_POST_RECORD_PRICES = [
    {
        "name": "record_single_price_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            }
        ]
    },
    {
        "name": "record_multiple_price_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "2.00",
                "response_code": 201
            }
        ]
    },
    {
        "name": "record_multiple_price_for_multiple_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "2.00",
                "response_code": 201
            },
            {
                "endpoint": "/products/register",
                "product_id": "2",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/2",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "2",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "2",
                "product_price": "2.00",
                "response_code": 201
            }
        ]
    },
    {
        "name": "record_multiple_indentical_price_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "2.00",
                "response_code": 201
            }
        ]
    },
    {
        "name": "record_single_price_for_single_unregistered_product",
        "queries": [
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 404,
                "response_message": "Product ID '1' has not been registered. Please register it with `/products/register`."
            }
        ]
    },
    {
        "name": "record_single_price_for_multiple_registered_and_unregistered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "2",
                "product_price": "2.00",
                "response_code": 404,
                "response_message": "Product ID '2' has not been registered. Please register it with `/products/register`."
            }
        ]
    },
    {
        "name": "record_single_price_for_single_invalid_unregistered_product",
        "queries": [
            {
                "endpoint": "/prices/record",
                "product_id": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
                "product_price": "1.00",
                "response_code": 422
            }
        ]
    },
    {
        "name": "record_single_invalid_price_type_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "invalid_price",
                "response_code": 422
            }
        ]
    },
    {
        "name": "record_single_invalid_price_decimal_places_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.001",
                "response_code": 422
            }
        ]
    },
    {
        "name": "record_single_invalid_price_greater_than_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "-1.00",
                "response_code": 422
            }
        ]
    },
    {
        "name": "record_single_invalid_price_max_digits_for_single_registered_product",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "12345678910.00",
                "response_code": 422
            }
        ]
    }
]

@pytest.fixture(params = TEST_POST_RECORD_PRICES, ids = lambda x: x["name"])
def test_post_record_prices_input(request):
    return request.param


TEST_GET_PRICES_HISTORY_INPUT = [
    {
        "name": "get_single_price_for_single_registered_product",
        "product_id": "1",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            }
        ],
        "response_data": {
            "product_prices": [
                {
                    "product_price": 1.00
                }
            ],
            "response_code": 200
        }
    },
    {
        "name": "get_multiple_price_for_single_registered_price",
        "product_id": "1",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "2.00",
                "response_code": 201
            }
        ],
        "response_data": {
            "product_prices": [
                {
                    "product_price": 1.00
                },
                {
                    "product_price": 2.00
                }
            ],
            "response_code": 200
        }
    },
    {
        "name": "get_multiple_identical_price_for_single_registered_price",
        "product_id": "1",
        "queries": [
            {
                "endpoint": "/products/register",
                "product_id": "1",
                "product_name": "Test Product",
                "product_url": "https://example.com/product/1",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            },
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 201
            }
        ],
        "response_data": {
            "product_prices": [
                {
                    "product_price": 1.00
                },
                {
                    "product_price": 1.00
                }
            ],
            "response_code": 200
        }
    },
    {
        "name": "get_no_price_for_single_registered_product",
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
            "product_prices": [],
            "response_code": 200
        }
    },
    {
        "name": "get_single_price_for_single_unregistered_product",
        "product_id": "1",
        "queries": [
            {
                "endpoint": "/prices/record",
                "product_id": "1",
                "product_price": "1.00",
                "response_code": 404,
                "response_message": "Product ID '1' has not been registered. Please register it with `/products/register`."
            }
        ],
        "response_data": {
            "response_code": 404,
            "response_message": "Product ID '1' has not been registered. Please register it with `/products/register`."
        }
    },
    {
        "name": "get_single_price_for_single_invalid_registered_product",
        "product_id": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
        "queries": [
            {
                "endpoint": "/prices/record",
                "product_id": "123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960",
                "product_price": "1.00",
                "response_code": 422
            }
        ],
        "response_data": {
            "response_code": 422
        }
    }
]

@pytest.fixture(params = TEST_GET_PRICES_HISTORY_INPUT, ids = lambda x: x["name"])
def test_get_prices_history_input(request):
    return request.param
