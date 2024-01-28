# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
#
# input: “ablabdabdab”
#
# Output: „Tripled: ablabdabdabablabdabdabablabdabdab“
def func():
    m = input("enter smth")
    print(f"""
    input: {m}
    Output: Tripled: {m*3}
    """)
func()

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)
def weight():
    m = int(input("Weight: "))
    return m/6

print(weight())


#3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)
# მაგ. „2 * 6“. ფუნქცია დაშლის სტრიქონს split() ფუნქციის გამოყენებით. დათვლის და დააბრუნებს შედეგს. გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი. ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და დაპრინტოს)

def calculator():
    user = input("Enter the expression (e.g. '2 * 6'): ")

    split_user = user.split()

    if len(split_user) != 3:
        print("Invalid input. Please provide the expression in the correct format.")
        return

    first_number_str,operator,second_number_str = split_user

    try:
        first_number = float(first_number_str)
        second_number = float(second_number_str)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = first_number / second_number
    elif operator == '^':
        result = first_number ** second_number
    else:
        print("Invalid operator. Please use one of: +, -, *, /, ^")
        return

    print(f"The result of {user} is: {result}")
    return result

calculator()
