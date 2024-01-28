import os
#1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
def write_in_file():
    while True:
        text = input("Enter a sentence: ")
        if text == 'enough':
            break

        with open("test.txt", 'a') as file:
            file.write(f"{text}\n")

write_in_file()

#2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.
def create_file():
    folder_location = input("Enter the folder location: ")
    file_name = input("Enter the file name: ")

    try:
        if not folder_location:
            print("folder path is required")
        if not file_name:
            print("file name is required")

        if folder_location and file_name:
            with open(f"{folder_location}/{file_name}", 'w') as file:
                file.write(f"")

            files = os.listdir(folder_location)
            print(files)

    except Exception as e:
        print(e)

create_file()
