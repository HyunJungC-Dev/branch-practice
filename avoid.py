def some_func_1():
    return "hello"


def some_func_2(word):
    return word


if __name__ == '__main__':
    user_word = input("Type anything: ")
    print(some_func_2(user_word))
