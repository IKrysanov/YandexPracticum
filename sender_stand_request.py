import requests
import configuration
import data


def post_new_user():
    # print(data.user_body)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)
# post_new_user()


def post_new_client_kit(body):
    if data.AUTH_TOKEN == "":
        response = post_new_user()
        print(response.status_code)
        print(response.json())
        data.AUTH_TOKEN = response.json()["authToken"]
    headers_kits = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + data.AUTH_TOKEN
    }
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         json=body,
                         headers=headers_kits)

post_new_client_kit(data.user_body)