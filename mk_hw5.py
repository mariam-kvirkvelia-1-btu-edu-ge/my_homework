#1.ციკლისმეშვეობით3 მომხმარებელსშეაყვანინეინფორმაციასაკუთარისახელის, გვარისდაასაკისშესახებ. თითოეულიმომხმარებლისინფორმაციაშეინახეინდივიდუალურსიაში. შემდეგკისამივესიადაამატესაერთოცალრიელსიასსახელადconsumer_info. Input_ისმეშვეობითმომხმარებლისინდექსისშეყვანისშემთხვევაშიპროგრამამუნდადაბრუნოსარჩეულმომხმარებელზეინფორმაციაშემდეგნაირად: Name: EleneLastname: KhardavaAge: 21

username = []
lastname = []
user_age = []
consumer_info = []

for m in range(3):
    user_name = input("Enter Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))

    username.append(user_name)
    lastname.append(last_name)
    user_age.append(age)

    consumer_info.append({
        "Name": user_name,
        "Lastname": last_name,
        "Age": age
    })

indexx = int(input("მომხმარებლის ინდექსი"))
if 0 <= indexx:
    user = consumer_info[indexx]
    print(f"""
    Name: {user["Name"]}
    Lastname: {user["Lastname"]}
    Age: {user["Age"]}
    """)
else:
    print("404")


#2.მომხმარებელიდაარეგისტრირეონლაინპლატფორმაზეთუსახელისველიარიქნებაცარიელი, ხოლოპაროლი8 სიმბოლოზემეტიანტოლია. მისიმონაცემებიშეინახელისთში. შემდეგმიეცისაშუალებასცადოსპლატფორმაზეშესვლადაშეადარემისმიერშემოყვანილიინფორმაციასიაშიშენახულინფორმაციას. დაბეჭდეშესაბამისიმესიჯი.

user_name = input("Enter Name: ")
last_name = input("Last Name: ")
age = int(input("Age: "))
passwd = (input("Enter Password: "))

info = []

reg = True
if user_name != "":
    if len(passwd) >= 8:
        info.append({
            "User Name": user_name,
            "Last Name": last_name,
            "Age": age,
            "Password": passwd
        })
        print("Registration successful!")
        if reg:
            login_user_name = input("Enter Name: ")
            login_last_name = input("Last Name: ")
            login_age = int(input("Age: "))
            login_passwd = (input("Enter Password: "))

            if info:
                indexx = info[0]
                if (login_user_name == indexx["User Name"] and login_last_name == indexx["Last Name"] and login_age == indexx["Age"] and login_passwd == indexx["Password"]):
                    print("Login successful. Access granted!")
                else:
                    print("Error! Login failed")
            else:
                print("Error! Login failed")
    else:
        print("Error! Registration failed")
else:
        print("Error! Registration failed")




# 3.შექმენიჩაშენებულისია, რომელშიციქნებაშენახულიცნობილიმსახიობებისშესახებინფორმაცია. მომხმარებელსშემოჰყავსმსახიობისსახელიანგვარი. თუსიაშიმოიძებნამსახიობი, დაბეჭდამისშესახებარსებულიინფორმაციარეზუმისსახით.

actors_info = [
    {
        "Name": "Tom Hanks",
        "Birthdate": "July 9, 1956",
        "Birthplace": "Concord, California, U.S.",
        "Occupation": "Actor, Filmmaker",
        "Notable Movies": "Forrest Gump, Cast Away, Saving Private Ryan"
    },
    {
        "Name": "Meryl Streep",
        "Birthdate": "June 22, 1949",
        "Birthplace": "Summit, New Jersey, U.S.",
        "Occupation": "Actress",
        "Notable Movies": "The Devil Wears Prada, Sophie's Choice, The Iron Lady"
    },
]

search_actor = input("Enter the name of the actor: ")

found = False
for m in actors_info:
    if search_actor.lower() == m["Name"].lower():
        print(f"Information about {search_actor}:")
        print(f"Birthdate: {m['Birthdate']}")
        print(f"Birthplace: {m['Birthplace']}")
        print(f"Occupation: {m['Occupation']}")
        print(f"Notable Movies: {m['Notable Movies']}")
        found = True
        break
    else:
        print(f"Sorry, {search_actor} information is not available.")
