# # 1. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
#
# import random
#
# random_list = [random.randint(1, 100) for _ in range(10)]
# print("Original list:", random_list)
# random_list.sort()
# print("Sorted list:", random_list)
#
# # 2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).
#
# import random
#
# random_list = [random.randint(1, 100) for _ in range(10)]
# print("Original list:", random_list)
#
# sorted_descending = sorted(random_list, reverse=True)
# print("Sorted list in descending order:", sorted_descending)
#
#
#
# # 3. დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.
#
# import random
# import time
#
#
# def bubble_sort(mk):
#     return sorted(mk)
#
#
# def selection_sort(mk):
#     return sorted(mk)
#
# def generate_random_list(size):
#     return [random.randint(1, 10000) for _ in range(size)]
#
#
# sizes = [1000, 2000, 3000]
#
# for size in sizes:
#     random_list = generate_random_list(size)
#
#
#     start_time = time.time()
#     bubble_sorted_list = bubble_sort(random_list)
#     bubble_time = time.time() - start_time
#     print(f"Bubble Sort time for {size} items: {bubble_time:.6f} seconds")
#
#     start_time = time.time()
#     selection_sorted_list = selection_sort(random_list)
#     selection_time = time.time() - start_time
#     print(f"Selection Sort time for {size} items: {selection_time:.6f} seconds")
#     print("-------------------------")
#
# # *=*=*=*=*=*=* Happy New Year! Wishing you a year filled with joy, laughter, and endless possibilities. *=*=*=*=*=*=*
#
#
#
#







#
# mk = {1:10, 2:20}
# mk[3]=30
# mk.update({4:40})
# print(mk)

#
# import logging
# logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
#
# try:
#     a = [1,2,3,4,5]
#     b = "2"
#     print(a[b])
#
# except Exception as e:
#
#     logging.error(f'Error occurred: {e}')

# a = [1, 2, 3, 4, 5]
# b = "2"
# print(a[b])

import logging

logging.basicConfig(filename='venv/error_log.txt', level=logging.ERROR)

try:
    a = [1, 2, 3, 4, 5]
    b = "2"
    print(a[b])

except Exception as e:

    logging.error(f'Error occurred at line {e.__traceback__.tb_lineno}: {e}', exc_info=True)


