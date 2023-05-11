import requests


def test_ping_endpoint():
    response = requests.get("http://localhost:8080/ping")
    assert response.status_code == 200
    assert response.json() == {"response": "pong"}

def test_ping_endpoint_different_from_404():
    # proxies = {
    #     "http://myproxy-url.com:8080",
    #     "http://myproxy-url.com:8080"
    # }
    # response = requests.get("http://localhost:8080/ping", proxies=proxies)
    response = requests.get("http://localhost:8080/ping")
    assert response.status_code != 404
    assert response.json() == {"response": "pong"}
