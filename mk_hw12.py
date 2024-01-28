# 1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
def remove_duplicates(input_dict):
    unique_dict = {key: value for key, value in input_dict.items() if list(input_dict.values()).count(value) == 1}
    return unique_dict

original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
result_dict = remove_duplicates(original_dict)
print(result_dict)

# 2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.
def is_dict_empty(input_dict):
    return bool(input_dict)
empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print(is_dict_empty(empty_dict))
print(is_dict_empty(non_empty_dict))



# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}

def dictt(strin):
    d = {}
    for word in strin:
        if d.get(word):
            d[word] += 1
        else:
            d[word] = 1

    print(d)

strin = "racoon"
dictt(strin)

