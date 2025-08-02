
import requests as rq
import base64

def get_token(url, client_id, secret_id) -> None:
    client_credentials = f"{client_id}:{secret_id}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {client_credentials_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials" 
    }
    response = rq.post(url, data=data, headers=headers)

    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        return (response.status_code, response.text)