"""this file will be deleted. Not part of the framework
    to understand - how to read csv, excel, json"""

import pandas

# df = pandas.read_csv(filepath_or_buffer="../test_data/test_add_valid_employee.csv", delimiter=";")
# print(df)
# print(60 * "-")
# print(df.values)
# print(60 * "-")
# print(df.values.tolist())
# print(60 * "-")
#
# for i in df.index:
#     print(df.loc[i].tolist())

"""read excel file and convert to data frame"""

dframe = pandas.read_excel(io="../test_data/orange_test_data.xlsx", sheet_name="test_add_valid_employee")
print(dframe)