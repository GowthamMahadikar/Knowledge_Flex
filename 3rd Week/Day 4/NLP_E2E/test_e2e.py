
from app import app

def test_e2e_text_classification():
    client = app.test_client()

    response = client.post("/predict", json={
        "text": "Application crashes on login"
    })

    assert response.status_code == 200
    data = response.get_json()

    assert data["label"] in ["Bug", "Feature"]
    assert data["confidence"] > 0.5
