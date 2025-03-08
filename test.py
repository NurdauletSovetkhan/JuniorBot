from fastapi.testclient import TestClient
from main import app  # Импортируем приложение FastAPI

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    print(response.status_code)
    print(response.json())  # Логирование ответа
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
