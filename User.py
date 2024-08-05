class user:
    def __init__(self, schoolName, schoolAddress):
        self.schoolName = schoolName
        self.schoolAddress = schoolAddress
    def show(self):
        print("School Name: ", self.schoolName, "School Address: ",self.schoolAddress)

    def register(self,name,phone,email,password):
        return name,phone,email,password

    def login(self, email,password):
        if email == "test@gmail.com" and password == "abc":
            return True
        else:
            return False