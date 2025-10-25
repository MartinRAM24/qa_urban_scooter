import requests
import configuration
import data

def post_new_delivery(register_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_COURIER,
        json=register_body,
        headers=data.headers,
    )

def post_login_courier(login_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.LOGIN_COURIER,
        json=login_body,
        headers=data.headers,
    )

def delete_courier(id_delivery, courier_id):
    url = f"{configuration.URL_SERVICE}{configuration.DELETE_COURIER}/{courier_id}"
    return requests.delete(url, json=id_delivery, headers=data.headers)



