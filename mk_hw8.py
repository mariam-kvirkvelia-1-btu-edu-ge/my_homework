#1. დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.
def multiply_list_elements(lst, multiplier):
    multiplied_list = list(map(lambda x: x * multiplier, lst))
    return multiplied_list


original_list = [1, 2, 3, 4, 5]
multiplier = 3
result = multiply_list_elements(original_list, multiplier)


print("Original List:", original_list)
print(f"All elements multiplied by {multiplier}:", result)


# 2. დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)

def length_of_list_after_filter(names_list):
    filtered_list = list(filter(lambda name: name[0].isupper(), names_list))
    return len(filtered_list)

names = ['Alice', 'bob', 'Charlie', 'Dave', 'emma', 'Frank']

result_length = length_of_list_after_filter(names)

print("Original List of Names:", names)
print("Length after removing names starting with a lowercase character:", result_length)

# 3. დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
def sum_positive_negative(numbers_list):
    positive_numbers_sum = sum(filter(lambda x: x > 0, numbers_list))
    negative_numbers_sum = sum(filter(lambda x: x < 0, numbers_list))
    return positive_numbers_sum, negative_numbers_sum


numbers = [3, -5, 7, -2, 9, -4, -6, 1]
positive_sum, negative_sum = sum_positive_negative(numbers)


print("Original List of Numbers:", numbers)
print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)


def create_account(account_number, name):
    return {'account_number': account_number, 'name': name, 'balance': 0}


def deposit(account, amount):
    account['balance'] += amount
    print(f"Deposit of ${amount} successful. Current balance: ${account['balance']}")

# 4. დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
def login(account, entered_account_number, entered_name):
    try:
        if account['account_number'] == entered_account_number and account['name'] == entered_name:
            print("Login successful!")
            print(f"Account Number: {account['account_number']}")
            print(f"Name: {account['name']}")
            print(f"Balance: ${account['balance']}")
        else:
            raise ValueError("Invalid account number or name. Login failed.")
    except ValueError as e:
        print(e)



account_number = "12345"
name = "mk"

bank_account = create_account(account_number, name)


deposit_amount = 50
deposit(bank_account, deposit_amount)

entered_account_number = input("Enter your account number: ")
entered_name = input("Enter your name: ")

login(bank_account, entered_account_number, entered_name)


