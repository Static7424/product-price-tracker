def test_register_product(client, test_post_register_products_input):
    queries = test_post_register_products_input["queries"]

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


def test_get_product(client, test_get_product_input):
    product_id = test_get_product_input["product_id"]
    queries = test_get_product_input["queries"]
    response_data = test_get_product_input["response_data"]

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
        f"/products/{product_id}"
    )
    assert(response.status_code == response_data["response_code"])
    response_data.pop("response_code", None)
    if (response_data.get("response_message", None)):
        assert(response.json()["detail"] == response_data["response_message"])

    if (all(key in response_data for key in ["product_id", "product_name", "product_url"])):
        formatted_response = response.json()
        formatted_response.pop("id", None)
        assert(formatted_response == response_data)
