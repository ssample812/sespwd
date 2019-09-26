import pytest

@pytest.mark.parametrize("user,password,expected", [
	("samiscool54", "pass123", True),
	("catlover24", "cupcake2", False),
])

def test_login(user, password, expected):
	logins = {
		"samiscool54": "pass123",
		"crazyhat": "53241",
		"catlover24": "cupcake1",
	}

	assert logins[user] == password
