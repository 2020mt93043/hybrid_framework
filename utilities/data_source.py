from typing import List, Tuple

test_invalid_login_data: list[tuple[str, str, str]] = [("saul", "saul123", "Invalid credentials"),
                                                       ("kim", "kim123", "Invalid credentials"),
                                                       ("john", "john123", "Invalid credentials")]
test_add_valid_employee: list[tuple[str, str, str, str, str, str, str, str]] = [
    ('Admin', 'admin123', "John", "J", "wick", "999", "John wick", "John"),
    ('Admin', 'admin123', "Peter", "J", "wick", "888", "Peter wick", "Peter")]
