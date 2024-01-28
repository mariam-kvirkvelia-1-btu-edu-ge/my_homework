# # 1. ვიქტორინაშეადგინევიქტორინისპროგრამა. მომხმარებელსუნდადავუსვათკითხვა: “რომელიიმპერიისმიერაგებულიწყალ-მომარაგებისსისტემა(აკვედუკი) ფუნქციონირებსდღესაც?”სავარაუდოპასუხები: 1.შუმერთა2.სელჩუკთა3.რომის4.მონღოლთამომხმარებელმაუნდაშეიყვანოსსწორიპასუხისნომერიანთავადსწორიპასუხი. შეცდომისშემთხვევაშიიბეჭდება: „არა! სწორიპასუხიარომის!“სწორიპასუხისშემთხვევაშიიბეჭდება: „სწორია!“
#
# m = input(f"""რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა(აკვედუკი) ფუნქციონირებს დღესაც?
# სავარაუდო პასუხები:
# 1.შუმერთა
# 2.სელჩუკთა
# 3.რომის
# 4.მონღოლთა\n""")
#
# if m == "3" or m == "რომის":
#     print("სწორია!")
# else:
#     print("არა! სწორი პასუხია რომის!")
#
# # 2. ონლაინმაღაზიაპროგრამაგთავაზობსპროდუქტისსამკატეგორიას. მაგ.1.ლეპტოპები2.პერსონალურიკომპიუტერები3.მობილურებიმომხმარებელიირჩევსერთ-ერთს.პროგრამაითხოვსმაქსიმალურბიუჯეტსდაბიუჯეტისმიხედვითსთავაზობსმომხმარებელსკონკრეტულმოდელსარჩეულკატეგორიაში. (თითოკატეგორიაშიმინიმუმ3 პროდუქტიმაინცუნდაიყოს)თუბიუჯეტიძალიანმცირეა, პროგრამაბეჭდავს, რომამთანხაშიარგააჩნიაშემოთავაზება.
#
# k = int(input(f"""Category:
# 1.Laptops
# 2.Personal computers
# 3.Mobile phones
# """))
# m = int(input("Price: "))
#
# if m <= 500:
#     print("There is no offer in this amount")
#
# elif k == 1 and m <= 1000:
#     print("Dell XPS 13, Price: 800")
# elif k == 1 and m <= 2000:
#     print("HP Spectre x360, Price: 1050")
# elif k == 1 and m > 2000:
#     print("MacBook Air, Price: 2100")
#
# elif k == 2 and m <= 1000:
#     print("HP Pavilion, Price: 800")
# elif k == 2 and m <= 2000:
#     print("Dell Inspiron, Price: 1800")
# elif k == 2 and m > 2000:
#     print("Lenovo IdeaCentre, Price: 2002")
#
# elif k == 3 and m <= 1000:
#     print("Google Pixel 6, Price: 799")
# elif k == 3 and m <= 2000:
#     print("Samsung Galaxy S21, Price: 1001")
# elif k == 3 and m > 2000:
#     print("iPhone 13, Price: 2001")
#
# else:
#     print("404")
#
#
# # 3. ქუესთისშედგენა(Text Based Adventure Game)დაწერეერთმანეთშიჩასმულიif-elseკონსტრუქციებისგამოყენებითმარტივიტექსტზედაფუძნებულისათავგადასავლოთამაში.მაგ. თავიდანპროგრამაბეჭდავსმომხმარებლისადგილსამყოფელსდასთავაზობსმქომედებისრამდენიმევარიანტს. სხვადასხვაარჩევანისშემთხვევაშითამაშსხვადასხვანაირადვითარდება.
# choice = input(f"""
# Enter your choice (1/2/3):
# 1. You decide to explore the forest. okay, let's go.
# 2. You start walking towards the mountains.
# 3. You decide to enter a dark cave.
# """)
#
# if choice == "1":
#     print("You decide to explore the forest. okay, let's go")
#     m = input(f"""
#     What do you do?
#     1. Follow the path on the left
#     2. Follow the path on the right
#     """)
#     if m == "1":
#         print("You encounter a group of friendly animals.They guide you safely out of the forest. You win!")
#     elif m == "2":
#         print("You wander deeper into the forest and get lost. Game Over.")
#     else:
#         print("Invalid choice. Game Over.")
# elif choice == "2":
#     print("You start walking towards the mountains.")
#     k = input(f"""
#     What do you do?
#     1. Take the narrow path up the mountains
#     2. Follow the wider path around the mountains
#     """)
#     if k == "1":
#         print("You successfully climb the mountains and discover a hidden paradise. You win!")
#     elif k == "2":
#         print("The wider path leads to a dead end. Game Over.")
#     else:
#         print("Invalid choice. Game Over.")
# elif choice == "3":
#     print("You decide to enter a dark cave.")
#     n = input(f"""
#     What do you do?
#     1. Light a torch
#     2. Feel your way through the darkness")
#     """)
#     if n == "1":
#         print("With the torch, you discover hidden treasure inside the cave. You win!")
#     elif n == "2":
#         print("You stumble upon a trap and fall into a pit. Game Over.")
#     else:
#         print("Invalid choice. Game Over.")
# else:
#     print("Invalid choice. Game Over.")
#
#
# List of dictionaries to store information about actors
actors_info = [
    {
        "Name": "Tom Hanks",
        "Birthdate": "July 9, 1956",
        "Birthplace": "Concord, California, U.S.",
        "Occupation": "Actor, Filmmaker",
        "Notable Movies": ["Forrest Gump", "Cast Away", "Saving Private Ryan"]
    },
    {
        "Name": "Meryl Streep",
        "Birthdate": "June 22, 1949",
        "Birthplace": "Summit, New Jersey, U.S.",
        "Occupation": "Actress",
        "Notable Movies": ["The Devil Wears Prada", "Sophie's Choice", "The Iron Lady"]
    },
    # Add more dictionaries for other actors
]

# Function to search for an actor and display information
def search_actor_info(actor_name):
    found = False
    for actor in actors_info:
        if actor["Name"].lower() == actor_name.lower():
            print(f"Information about {actor_name}:")
            print(f"Birthdate: {actor['Birthdate']}")
            print(f"Birthplace: {actor['Birthplace']}")
            print(f"Occupation: {actor['Occupation']}")
            print("Notable Movies:")
            for movie in actor['Notable Movies']:
                print(f"- {movie}")
            found = True
            break

    if not found:
        print(f"Sorry, information about {actor_name} is not available.")

# User input for actor's name
search_actor = input("Enter the name of the actor: ")

# Call the function to search for the actor's information
search_actor_info(search_actor)
