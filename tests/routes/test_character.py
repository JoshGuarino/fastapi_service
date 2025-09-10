from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_character_quote():
    response = client.get("/character/Gandalf")
    assert response.status_code == 200
    assert isinstance(response.json(), str)

def test_character_not_found():
    response = client.get("/character/NotFound")
    assert response.status_code == 404
    assert response.json() == {"detail": "Character not found."}
