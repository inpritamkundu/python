
#  Using Pandas
# import pandas as pd

# # Reading entire file
# data = pd.read_excel(
#     r'C:\Users\Gautam\Downloads\session 1 Budding Entrepreneurs _ India is waiting for startups to innovate (Responses) (1).xlsx')

# # Reading a column
# df = pd.DataFrame(data, columns=['First Name'])
# print(df[0])


# Using xlrd

import xlrd
path = r'C:\Users\Gautam\Downloads\session 1 Budding Entrepreneurs _ India is waiting for startups to innovate (Responses) (1).xlsx'
# Give the location of the file
loc = (path)

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
print(sheet.cell_value(1, 2)+sheet.cell_value(1, 3))
