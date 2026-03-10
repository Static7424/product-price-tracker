def test_post_record_prices(client, test_post_record_prices_input):
    queries = test_post_record_prices_input["queries"]
    
    for query in queries:
        endpoint = query.pop("endpoint")
        expected_response_code = query.pop("response_code")
        expected_response_message = query.pop("response_message", None)
        
        response = client.post(
            endpoint,
            data = query
        )
        
        assert(response.status_code == expected_response_code)
        if (expected_response_message):
            assert(response.json()["detail"] == expected_response_message)


def test_get_prices_history(client, test_get_prices_history_input):
    product_id = test_get_prices_history_input["product_id"]
    queries = test_get_prices_history_input["queries"]
    response_data = test_get_prices_history_input["response_data"]
    
    for query in queries:
        endpoint = query.pop("endpoint")
        expected_response_code = query.pop("response_code")
        expected_response_message = query.pop("response_message", None)
        
        response = client.post(
            endpoint,
            data = query
        )
        
        assert(response.status_code == expected_response_code)
        if (expected_response_message):
            assert(response.json()["detail"] == expected_response_message)

    response = client.get(
        f"/prices/{product_id}/history"
    )
    assert(response.status_code == response_data["response_code"])
    if (response_data.get("response_message", None)):
        assert(response.json()["detail"] == response_data["response_message"])

    if (response_data.get("product_prices", None)):
        formatted_response = []
        for price in response.json()["product_prices"]:
            price.pop("id", None)
            price.pop("recorded_at", None)
            formatted_response.append(price)
        
        assert(formatted_response == response_data["product_prices"])