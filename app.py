import requests
import time
from add_items import add_items_to_order

url = "https://cashierc.pharmaco-medica.com/api/machine-status"

payload = {}
headers = {}

while True:
    response = requests.request("GET", url, headers=headers, data=payload)
    json_response = response.json()

    order_number = None

    # Check the value of the "status" key
    if "status" in json_response:
        if json_response["status"] == 1:
            order_number = json_response["order_number"]
            # send model function
            print(order_number)
            # machine ON function

            # send

            # CONDITION
            response_text = add_items_to_order(order_number)

            print(response_text)
            #

        else:
            print("track not working")
    else:
        print("Invalid JSON structure")

    # delay by 10 seconds
    time.sleep(10)
