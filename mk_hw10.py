# 1. დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.
#
# 2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.
#
# 3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.
#
# 4. დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებშ

import random
import time

def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]

def sort_list(mk):
    return sorted(mk)

def linear_search(mk, target):
    for i, num in enumerate(mk):
        if num == target:
            return i
    return -1
def binary_search(mk, target):
    low = 0
    high = len(mk) - 1

    while low <= high:
        mid = (low + high) // 2
        if mk[mid] == target:
            return mid
        elif mk[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result

    return wrapper

@calculate_execution_time
def perform_linear_search(mk, target):
    return linear_search(mk, target)

@calculate_execution_time
def perform_binary_search(mk, target):
    return binary_search(mk, target)

small_list = generate_random_list(100)
medium_list = generate_random_list(1000)
large_list = generate_random_list(10000)

sorted_small = sort_list(small_list)
sorted_medium = sort_list(medium_list)
sorted_large = sort_list(large_list)

target_small = random.choice(sorted_small)
target_medium = random.choice(sorted_medium)
target_large = random.choice(sorted_large)

print(f"Searching for {target_small} in small list:")
perform_linear_search(sorted_small, target_small)
perform_binary_search(sorted_small, target_small)

print(f"\nSearching for {target_medium} in medium list:")
perform_linear_search(sorted_medium, target_medium)
perform_binary_search(sorted_medium, target_medium)

print(f"\nSearching for {target_large} in large list:")
perform_linear_search(sorted_large, target_large)
perform_binary_search(sorted_large, target_large)
