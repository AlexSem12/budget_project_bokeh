import pandas as pd
import datetime as dt

# Parameters
year_start = 2010
year_end = 2020
start_income_amount = 40000
budget_type = 'Increasing'
growth_rate = 0.2
expense_proportion = 0.8
expense_categories_list = ['Food', 'Rent', 'Entertainment', 'Home Improvements', 'Car', 'Internet', 'Cell Phone',
                           'Health', 'Insurance', 'Services']
expense_categories_proportion = {'Food': 0.15, 'Rent': 0.25, 'Entertainment': 0.1, 'Home Improvements': 0.1,
                                 'Car': 0.05, 'Internet': 0.05, 'Cell Phone': 0.05, 'Health': 0.1, 'Insurance': 0.15,
                                 'Services': 0.5}
income_categories_list = ['Salary', 'Cash Backs', 'Miscellaneous']
income_categories_proportion = {'Salary': 0.8, 'Cash Backs': 0.05, 'Miscellaneous': 0.15}
cost_center_list = ['husband', 'wife']
cost_center_proportion = {'husband': 0.7, 'wife': 0.3}
file_income_columns = ['Date', 'Category', 'Description', 'Cost Center', 'Amount', 'Currency', 'Exchange Rate',
                       'Amount USD', 'Year', 'Month', 'Quarter']
file_expense_columns = ['Date', 'Category', 'Subcategory', 'Item', 'Units', 'Units number', 'Unit price',
                        'Currency', 'Amount', 'Exchange Rate', 'Amount USD', 'Place', 'Year', 'Quarter',
                        'Month', 'Week', 'Weekday', 'Cost Center']

print('Budget start year: ' + str(year_start))
print('Budget end year: ' + str(year_end))
print('Number of years: ' + str(year_end - year_start))
print('Starting income: ' + str(start_income_amount))
print('Budget type: ' + str(budget_type))
print('Budget growth rate: ' + str(growth_rate))
print('Expense proportion: ' + str(expense_proportion))
print('Expense categories: ' + str(expense_categories_list))
print('Income categories: ' + str(income_categories_list))
print('Cost centers: ' + str(cost_center_list))

# income generation
income_matrix = pd.DataFrame(columns=file_income_columns)
year_income = start_income_amount
year = year_start
for i in range(0, year_end - year_start + 1):
    for month in range(1, 13):
        for category in income_categories_list:
            for cost_center in cost_center_list:
                amount = (year_income / 12) * income_categories_proportion[category] * cost_center_proportion[
                    cost_center]
                first_raw = pd.DataFrame([[dt.date(year, month, 1), category, 'Description', cost_center, amount,
                                           'USD', '1', amount, year, month,
                                           pd.Timestamp(dt.date(year, month, 1)).quarter]], columns=file_income_columns)
                income_matrix = pd.concat([first_raw, income_matrix], ignore_index=True)
    year = year + 1
    year_income = year_income + year_income * growth_rate

print(income_matrix)

# expense generation
expense_matrix = pd.DataFrame(columns=file_expense_columns)
year_expense = start_income_amount * expense_proportion
year = year_start
for i in range(0, year_end - year_start + 1):
    for month in range(1, 13):
        for category in expense_categories_list:
            for cost_center in cost_center_list:
                amount = (year_expense / 12) * expense_categories_proportion[category] * cost_center_proportion[
                    cost_center]
                first_raw = pd.DataFrame([[dt.date(year, month, 1), category, 'subcategory', 'item', 'unit',
                                           '1', amount, 'USD', amount, '1', amount, 'Place', year,
                                           pd.Timestamp(dt.date(year, month, 1)).quarter, month,
                                           pd.Timestamp(dt.date(year, month, 1)).week,
                                           pd.Timestamp(dt.date(year, month, 1)).weekday, cost_center]],
                                         columns=file_expense_columns)
                expense_matrix = pd.concat([first_raw, expense_matrix], ignore_index=True)
    year = year + 1
    year_expense = year_expense + year_expense * growth_rate


# writing a file
writer = pd.ExcelWriter('test_file.xlsx', engine='xlsxwriter')
income_matrix.to_excel(writer, 'Income', columns=file_income_columns, index=False)
expense_matrix.to_excel(writer, 'Expenses', columns=file_expense_columns, index=False)
writer.save()
