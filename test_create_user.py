import sender_stand_request as api
import data
import copy
import pytest

def make_order_body(**overrides):
    body = copy.deepcopy(data.order_body)
    body.update(overrides)
    return body

def make_register_body(**overrides):
    body = copy.deepcopy(data.register_body)
    body.update(overrides)
    return body

def make_login_body(**overrides):
    body = copy.deepcopy(data.login_body)
    body.update(overrides)
    return body

def create_and_fetch_order(body: dict) -> dict:
    response = api.create_new_order(body)
    assert response.status_code == 201
    track = response.json()["track"]
    resp_check = api.check_order_create(track)
    assert resp_check.status_code == 200
    return resp_check.json()["order"]

def assert_field_accepts(field: str, value):
    order = create_and_fetch_order(make_order_body(**{field: value}))
    assert order[field] == value

def assert_field_not_accepts(field: str, value):
    r = api.create_new_order(make_order_body(**{field: value}))
    assert r.status_code == 400

def get_courier_id(field: str, value):
    resp = api.post_login_courier(make_login_body(**{field: value}))
    assert resp.status_code == 200
    return resp.json()["id"]

def positive_assert_create(field: str, value):
    resp = api.post_new_delivery(make_register_body(**{field: value}))
    assert resp.status_code == 201

def positive_assert_login(field: str, value):
    resp = api.post_login_courier(make_login_body(**{field: value}))
    assert resp.status_code == 200

def positive_delete_courier(field: str, value):
    resp_login = api.post_login_courier(make_login_body(**{field: value}))
    assert resp_login.status_code == 200
    courier_id = resp_login.json()["id"]
    delete_body = data.id_delivery.copy()
    delete_body["id"] = str(courier_id)
    resp_delete = api.delete_courier(delete_body, courier_id)
    assert resp_delete.status_code == 200
    resp_check = api.delete_courier(delete_body, courier_id)
    assert resp_check.status_code == 404



#firtsName
@pytest.mark.parametrize("v", ["Fe", "Luz", "Jose Jesus", "Jose_Francisco", "Jorge Francisco"])
def test_firstname_ok(v):
    assert_field_accepts("firstName", v)

@pytest.mark.parametrize("v", ["","Jesus34","名Jose","J@ose", "Sandra Yosseline","s"])
def test_firstname_fail(v):
    assert_field_not_accepts("firstName", v)





#Login
@pytest.mark.parametrize("v", ["abd", "abcdefr"])
def test_create_user_4_chars(v):
    positive_assert_create("login", v)
    positive_assert_login("login", v)
    positive_delete_courier("login", v)


