from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_existing_participant():
    activity_name = "Chess Club"
    email = "student@example.com"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert delete_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_missing_participant():
    activity_name = "Chess Club"
    email = "missing@example.com"

    response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert response.status_code == 404
