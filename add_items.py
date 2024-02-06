import requests
import json


def add_items_to_order(order_number):
    url = "https://cashierc.pharmaco-medica.com/api/orders/add-items"

    payload = json.dumps(
        {
            "order_number": order_number,
            "items": [
                {"product_sku": "F-1", "quantity": 10},
                {"product_sku": "st-1", "quantity": 5},
            ],
        }
    )

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)

    return response.text
