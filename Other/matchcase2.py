
import requests


def http_status(status: int):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404: 
            return "Not found"

print(f"Status: {http_status(401)}")


class Switch:
    on = 1
    off = 0

status = 1

match status:
    case Switch.on:
        print("ON!")
    case Switch.off:
        print('OFF!')