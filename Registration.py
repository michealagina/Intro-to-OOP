from User import user

jane =user("Bingham University","Karu, Nasarawa")
jane.show()

#user = User()
#user.register("james","111","abc","abc"

email = input("Enter Email: ")

password = input("Enter Password: ")
print(user.login(email, password))