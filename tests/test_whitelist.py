from whitelist import realName, validate_server

def test_whitelist_name() -> None:
    name = "Brr1"
    assert realName(name) == 'Bruno'

def test_outer_name() -> None:
    name = "John"
    assert realName(name) == name

def test_valid_server() -> None:
    server = 'euw'
    assert validate_server(server) == server

def test_invalid_server() -> None:
    invalid_server = 'lit'
    assert validate_server(invalid_server) == 'euw'