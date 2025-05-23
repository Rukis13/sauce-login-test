import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def test_create_post():
    response = requests.post(URL, json={"title": "foo", "body": "bar", "userId": 1})
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_update_post():
    response = requests.put(f"{URL}/1", json={"id": 1, "title": "updated", "body": "bar", "userId": 1})
    assert response.status_code == 200
    assert response.json()["title"] == "updated"

def test_delete_post():
    response = requests.delete(f"{URL}/1")
    assert response.status_code in [200, 204]
    