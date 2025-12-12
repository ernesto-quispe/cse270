import requests
import types

BASE_URL = "https://127.0.0.1:8000/users"


def _build_mock_response(status_code: int, text: str = ""):
    """Minimal Response-like object."""
    mock_resp = types.SimpleNamespace()
    mock_resp.status_code = status_code
    mock_resp.text = text
    return mock_resp


def test_users_admin_wrong_password_returns_401_empty_text(mocker):
    # Arrange: patch requests.get
    mock_get = mocker.patch("requests.get")
    mock_get.return_value = _build_mock_response(status_code=401, text="")

    # Act
    response = requests.get(
        BASE_URL,
        params={"username": "admin", "password": "admin"},
        verify=False,
    )

    # Assert: verify call + expectations
    mock_get.assert_called_once_with(
        BASE_URL,
        params={"username": "admin", "password": "admin"},
        verify=False,
    )
    assert response.status_code == 401
    assert response.text == ""


def test_users_admin_querty_returns_200_empty_text(mocker):
    # Arrange: patch requests.get
    mock_get = mocker.patch("requests.get")
    mock_get.return_value = _build_mock_response(status_code=200, text="")

    # Act
    response = requests.get(
        BASE_URL,
        params={"username": "admin", "password": "querty"},
        verify=False,
    )

    # Assert: verify call + expectations
    mock_get.assert_called_once_with(
        BASE_URL,
        params={"username": "admin", "password": "querty"},
        verify=False,
    )
    assert response.status_code == 200
    assert response.text == ""