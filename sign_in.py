from firebase_admin import auth
import getpass
import json
  
class sign_in:
    def __init__(self):
        self.json_password = "0"
        self.password_correct = False
        self.user_name = "0"


    def authenticate_user(self):
        while self.user_name == "0":
            email = input("Enter Email: ")
            self.identify_user(email)

        while self.json_password == "0" or not self.password_correct:
            self.get_password()
            self.verify_password()

        print(f"Hello {self.user_name}\n")
        return self.user_name
    
    def identify_user(self, email):
        for user in auth.list_users().iterate_all():
            if email == user.email:
                self.user_name = user.display_name
                return self.user_name
        print("Incorrect email - No Capital Letters")
        return self.user_name
        

    def get_password(self):
        # Opening JSON file
        with open('passwords.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            integer_counter = 0
            for i in json_object["users"]:
                if json_object["users"][integer_counter]["name"] == self.user_name:
                    self.json_password = json_object["users"][integer_counter]["password"]
                    return self.json_password
                integer_counter += 1
        print(">.< Could not find a database user by that email! Try again :D")
        return self.json_password
        
    def verify_password(self):
        password = getpass.getpass(prompt='Password: ', stream=None)
        if self.json_password == password:
            self.password_correct = True
            return self.password_correct
        else:
            print(">.< Incorrect password! Try Again.")
            self.password_correct = False
            return self.password_correct

        
    
        