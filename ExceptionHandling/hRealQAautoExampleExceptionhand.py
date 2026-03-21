def get_test_data(index):
    data= ["login", "signup"]
    try:
        return data[index]
    except IndexError:
        return "Invalid test case index"
        
print(get_test_data(0))