def test_register_product(client):
    response = client.post(
        "/products/regsiter",
        json = {
            "product_id": "1",
            "name": "Test Product"
        }
    )
    
    assert (response.status_code == 200)
