from starlette.testclient import TestClient
from post import app

# get and assign app to create test client
client = TestClient(app)


def test_read_declare_request_body():
    response = client.post(
        "/post",
        json={
            "string": "foo",
            "lists": [1, 2],
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "text": "hello, foo, None, [1, 2]",
    }
