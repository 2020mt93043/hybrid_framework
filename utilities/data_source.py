from typing import List, Tuple
from utilities import read_utils

# Import data from another file
# test_invalid_login_data: list[tuple[str, str, str]] = [("saul", "saul123", "Invalid credentials"),
#                                                        ("kim", "kim123", "Invalid credentials"),
#                                                        ("john", "john123", "Invalid credentials")]
test_add_valid_employee: list[tuple[str, str, str, str, str, str, str, str]] = [
    ('Admin', 'admin123', "John", "J", "wick", "999", "John wick", "John"),
    ('Admin', 'admin123', "Peter", "J", "wick", "888", "Peter wick", "Peter")]

# Import data from csv
test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_add_valid_employee.csv")