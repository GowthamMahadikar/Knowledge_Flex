# pytest api tests
import requests

BASE_URL = "http://127.0.0.1:5000"


def test_404_not_found():
    r = requests.get(f"{BASE_URL}/invalid")
    assert r.status_code == 404


def test_405_method_not_allowed():
    r = requests.put(f"{BASE_URL}/tasks")
    assert r.status_code == 405


def test_create_task():
    r = requests.post(f"{BASE_URL}/tasks", json={"title": "Test"})
    assert r.status_code in [200, 201]


def test_get_tasks():
    r = requests.get(f"{BASE_URL}/tasks")
    assert r.status_code == 200


def test_update_task():
    r = requests.put(f"{BASE_URL}/tasks/1", json={"status": "Done"})
    assert r.status_code in [200, 204]


def test_delete_task():
    r = requests.delete(f"{BASE_URL}/tasks/1")
    assert r.status_code in [200, 204, 404]
