headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

register_body = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

login_body = {
    "login": "ninja",
    "password": "1234"
}

id_delivery = {"id": "1"}

def make_register_body(login: str, password: str, first_name: str):
    b = register_body.copy()
    b["login"] = login
    b["password"] = password
    b["firstName"] = first_name
    return b

def make_login_body(login: str, password: str):
    b = login_body.copy()
    b["login"] = login
    b["password"] = password
    return b
