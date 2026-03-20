user = {"name":"Papun",
        "age":32,
        "role":"QA"}
print(user)

#Add
user["City"]= "Bhubaneswar"
print(user)

#Update
user["age"]= 33

#Remove
del user["role"]

print(user)