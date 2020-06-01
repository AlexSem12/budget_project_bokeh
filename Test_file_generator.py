import pandas as pd

# Parameters
year_start = 2010
year_end = 2020
start_income_amount = 40000
budget_type = 'Increasing'
growth_rate = 0.2
expense_proportion = 0.8
expense_categories = ['Food', 'Rent', 'Entertainment', 'Home Improvements', 'Car', 'Internet', 'Cell Phone', 'Health',
                      'Insurance']
income_categories = ['Salary', 'Cash Backs', 'Miscellaneous']
cost_centers = ['husband', 'wife']

print('Budget start year: ' + str(year_start))
print('Budget end year: ' + str(year_end))
print('Starting income: ' + str(start_income_amount))
print('Budget type: ' + str(budget_type))
print('Budget growth rate: ' + str(growth_rate))
print('Expense proportion: ' + str(expense_proportion))
print('Expense categories: ' + str(expense_categories))
print('Income categories: ' + str(income_categories))
print('Cost centers: ' + str(cost_centers))

writer = pd.ExcelWriter('test_file.xlsx', engine='xlsxwriter')


final_matrix = pd.DataFrame()

final_matrix.to_excel(writer,'Sheet1')
writer.save()