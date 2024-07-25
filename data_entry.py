from datetime import datetime as dt

CATEGORIES = {'I':"Income", 'E':"Expense"}

def get_date(prompt, allow_default=False):
    datestr = input(prompt)
    if allow_default and not datestr:
        return dt.today().strftime("%d-%m-%Y")
    try:
        valid_date = dt.strptime(datestr, "%d-%m-%Y")
        return valid_date
    except ValueError:
        print("Invalid date format. Please enter date in dd-mm-yyyy format")
        return(get_date("Enter date: ", allow_default))
    
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be more than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category  = input("Enter a category ( 'I' for income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    return get_category()

def get_description():
    return input("Enter description (optional): ")