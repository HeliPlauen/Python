
import requests


def check_connect(status: int):
    match status:
        case status if status >= 200 and status < 300:
            return f"Good request {status}"
        case _: 
            return f"Bad request {status}"


def check_headers(resp:dict):
    match resp:
        case {"Content-Type": content_type}:
            return f"Content-Type: {content_type}"


response = requests.get("https://google.com")
print(check_connect(response.status_code))
resp_json = response.headers
print(resp_json)
print(check_headers(resp_json))


