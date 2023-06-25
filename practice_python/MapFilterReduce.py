users = [
{'firstName': "donald", 'lastName': "trump", 'age': 75, 'salary':1002 }, 
{'firstName': "akshay", 'lastName': "saini", 'age': 26, 'salary':1001 },
{'firstName': "elon", 'lastName': "musk", 'age': 50, 'salary':1003 },
{'firstName': "deepika", 'lastName': "padukone", 'age': 26, 'salary':1004 }
];


# Git the Full name of the user whose age is less than 30

# using normal function
def age30Filter(data) :
    if data['age'] <= 30:
        return data

def fullName(data) :
    user_data = {
            "Name":data['firstName'] + ' ' + data['lastName']
        }
    return user_data


user_data_age_till_30 = list(filter(age30Filter, users))
print("\nUse of Filter : ")
print(user_data_age_till_30)

user_fullName = list(map(fullName, user_data_age_till_30))
print("\nUse of Map on filter : ")
print(user_fullName)





# using Lambda function
print(" using Lambda function ")
user_data_age_till_30 = list(filter(lambda data : data['age'] >= 30 , users))
print("\nUse of Filter : ")
print(user_data_age_till_30)

user_fullName = list(map(lambda data : {'FName': data['firstName'] + ' ' + data['lastName']}, user_data_age_till_30))
print("\nUse of Map on filter : ")
print(user_fullName)
