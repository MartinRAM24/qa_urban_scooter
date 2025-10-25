import sender_stan_request as api
import data

def get_courier_id(login: str, password: str) -> int:
    login_body = data.make_login_body(login, password)
    resp = api.post_login_courier(login_body)
    assert resp.status_code == 200, f"Login falló: {resp.status_code} {resp.text}"
    return resp.json()["id"]

def get_delete_courier(login: str, password: str):
    courier_id = get_courier_id(login, password)
    delete_body = data.id_delivery.copy()
    delete_body["id"] = str(courier_id)
    resp_delete = api.delete_courier(delete_body, courier_id)
    return resp_delete

def positive_assert_create(login, password, first_name):
    reg_body = data.make_register_body(login, password, first_name)
    resp = api.post_new_delivery(reg_body)
    assert resp.status_code == 201

def positive_assert_login(login, password):
    login_body = data.make_login_body(login, password)
    resp = api.post_login_courier(login_body)
    assert resp.status_code == 200

def test_create_user_4_chars():
    login = "abcd"
    password = "1234"
    positive_assert_create(login, password, "Juan")
    positive_assert_login(login, password)
    r = get_delete_courier(login, password)
    assert r.status_code in (200, 204)

def test_create_user_10_chars():
    login = "abcdefghij"
    password = "1234"
    positive_assert_create(login, password, "Pedro")
    positive_assert_login(login, password)
    r = get_delete_courier(login, password)
    assert r.status_code in (200, 204)