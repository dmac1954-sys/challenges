def main():
    user_list = [1,'b', 3, 3, 5, 6, 'a', 'b', 'c']
    print(list_filter(user_list))

def list_filter(user_list):
    new_list = []
    for item in user_list:
        if type(item) == int:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    main()