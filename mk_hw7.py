#1. რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)

def rec(times, text):
    if times > 0:
        print(text)
        rec(times - 1, text)

number = 5
text = "Hello, world!"
rec(number, greeting)

# 2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.

def restaurant():
    try:
       order = input("Order: ")
       quantity = int(input("Quantity: "))
       if quantity is None:
           quantity = 1
       else:
            print(f"Order: {quantity} {order}")
    except:
        print("Invalid quantity. Defaulting to quantity = 1.")
        quantity = 1
        print(f"Order: {quantity} {order}")

restaurant()

# 3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს
def calc():
    numbers = input("Numbers (separated by space): ")
    splitt = numbers.split()
    if len(splitt) != 3:
        print("Invalid input: Please provide exactly three numbers separated by spaces.")
        return

    first_number_str, second_number_str, third_number_str = splitt

    try:
        first_number = float(first_number_str)
        second_number = float(second_number_str)
        third_number = float(third_number_str)

        result = first_number * second_number * third_number
        print(f"Result is: {result}")
        return result
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None

calc()
