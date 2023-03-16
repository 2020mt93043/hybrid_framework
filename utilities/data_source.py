from typing import List, Tuple
from utilities import read_utils

# Import data from another file
# test_invalid_login_data: list[tuple[str, str, str]] = [("saul", "saul123", "Invalid credentials"),
#                                                        ("kim", "kim123", "Invalid credentials"),
#                                                        ("john", "john123", "Invalid credentials")]
# test_add_valid_employee: list[tuple[str, str, str, str, str, str, str, str]] = [
#     ('Admin', 'admin123', "John", "J", "wick", "999", "John wick", "John"),
#     ('Admin', 'admin123', "Peter", "J", "wick", "888", "Peter wick", "Peter")]

# Import data from csv
test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_add_valid_employee.csv")

# import test data from excel
test_add_valid_employee = read_utils.get_sheet_as_list("../test_data/orange_test_data.xlsx", "test_add_valid_employee")

# import test data from excel to upload wrong file to profile photo
test_invalid_profile_upload = read_utils.upload_wrong_file_profile_photo("../test_data/orange_test_data.xlsx", "test_invalid_profile_upload")

# import test data from json file
test_get_value_from_json = read_utils.get_value_from_json("../test_data/data.json", "browser")