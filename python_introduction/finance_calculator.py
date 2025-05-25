#pseudocode to for script to for personal finance calculator
#prompt users for personal information
#prompt users to input  monthly  income
#prompt users to input monthly  expenses
#calculate savings by  subtracting expenses from income
#interest rate on  savings is 5%
# calculate the projected savings  after one year = monthly savings *  12  + ( monthly savings *12) * 0.05
# collecting user infor


first_name = input('Enter Your first name :')
last_name = input('Enter Your last name :')
age = float(input('Enter Your age :'))
gender = input('Enter Your Gender :')
job = input('Enter Your Job :')


#collecting user income and expenses
monthly_income = float(input('Enter your monthly income:'))
monthly_expenses = float(input('Enter your total monthly expenses:'))

# declaring interest rate
interest_rate = 0.05  # 5%
# Saving function to compute saving
monthly_savings = monthly_income - monthly_expenses

# calculating the projected savings after one year

projected_saving = monthly_savings * 12  + (monthly_savings * 12 ) * interest_rate

# displaying output
print(first_name)
print(last_name)
print(age)
print(gender)
print(job)
print( monthly_income)
print( monthly_expenses)
print( monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_saving)