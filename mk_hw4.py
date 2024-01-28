#1.მომხმარებელსშემოაყვანინეინფორმაციადადათვალერამდენირიცხვი, ანბანისასოდასხვასიმბოლოამოცემულიწინადადებაში. შედეგიდაბეჭდე.გამოიყენეforციკლი, isalphaდაisdigitფუნქციები.

m = input("Enter Information: ")

number_count = 0
letter_count = 0
other_count = 0

for i in m:
    if i.isdigit():
        num_count += 1
    elif i.isalpha():
        letter_count += 1
    else:
        other_count += 1

print(f"Number of numbers: {num_count}")
print(f"Number of letters: {letter_count}")
print(f"Number of other symbols: {other_count}")
#
# #2.მომხმარებელსშეაყვანინეორიწინადადებადამათგანშეადგინემესამეშემდეგწესებზედაყრდნობით. შექმნილიწინადადებაუნდაიწყებოდესპირველიწინადადებისპირველისიმბოლოთი, რომელსაცჯერმოჰყვებამეორეწინადადებისბოლოსიმბოლო, შემდეგკიპირველიწინადადებისმეორესიმბოლოდამეორეწინადადებისბოლოდანმეორესიმბოლო
#
# m1 = input("Enter the first sentence: ")
# m2 = input("Enter the second sentence: ")
#
# if len(m1) > 0 and len(m2) > 0:
#     new_sentence = m1[0] + m2[-1] + m1[1] + m2[-1]
#     print(f"New sentence is: {new_sentence}")
# else:
#     print("404")
#
# # 3.მომხმარებელსშეაყვანინეორიწინადადებადაშეამოწმე, პირველწინადადებაშიარსებულიყველასიმბოლოთუშედისმეორეწინადადებაშიდაპირიქით, მეორეწინადადებაშიშემავალიყველასიმბოლოთუშედისპირველწინადადებაში. თუესორიპირობადაკმაყოფილდა, დაბეჭდე:„Strings are balanced!“თურომელიმეპირობადაირღვა, დაბეჭდე:„Strings are not balanced!“
#
# m1 = input("Enter the first sentence: ")
# m2 = input("Enter the second sentence: ")
#
# if set(m1) == set(m2):
#     print("Strings are balanced!")
# else:
#     print("Strings are not balanced!")
#
