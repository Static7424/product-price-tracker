def test_register_product(client):
    response = client.post(
        "/products/register",
        data={
            "product_id": "1",
            "product_name": "Test Product",
            "product_url": "https://example.com/product/1",
        },
    )

    assert response.status_code == 201
