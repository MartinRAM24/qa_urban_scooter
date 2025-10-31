import requests
import configuration
import data


def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body,
                         headers=data.headers,)

def check_order_create(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS,
                        params={"t": track},
                        headers=data.headers)

def post_new_delivery(register_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER,
        json=register_body,
        headers=data.headers,
    )

def post_login_courier(login_body):
    return requests.post(configuration.URL_SERVICE + configuration.LOGIN_COURIER,
        json=login_body,
        headers=data.headers,
    )

def delete_courier(id_delivery, courier_id):
    url = f"{configuration.URL_SERVICE}{configuration.DELETE_COURIER}/{courier_id}"
    return requests.delete(url, json=id_delivery, headers=data.headers)



