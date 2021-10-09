from firebase_admin import auth
import getpass
import json
  
class sign_in:
    def __init__(self):
        #set while loop conditions
        self.json_password = "0"
        self.password_correct = False
        self.user_name = "0"


    def authenticate_user(self):
        while self.json_password == "0": # while the user_name couldn't be found in the json file!  
            while self.user_name == "0":
                #get user email
                email = input("Enter Email: ")
                #iterates through database users to see if there is a matching email. This returns the user_name
                self.identify_user(email)

            while not self.password_correct: # the password isn't correct
                # searches the json file and returns json_password that corrisponds to the user's name
                self.get_password()
                # compares the json_password and the user-inputted password
                self.verify_password()

        print(f"Hello {self.user_name}\n")
        return self.user_name
    
    def identify_user(self, email):
        #iterates through database users to see if there is a matching email. This returns the user_name
        for user in auth.list_users().iterate_all():
            if email == user.email: #if email on file matches user inputted email
                self.user_name = user.display_name  #then get that user's name
                return self.user_name #return the user's name
        print("Incorrect email - Do Not Use Capital Letters") #if name not found + helpful hint
        return self.user_name #returns "0"
        

    def get_password(self):
        # searches the json file and returns json_password that corrisponds to the user's name
        # I learned a lot about json files too!!
        # Opening JSON file
        with open('passwords.json', 'r') as openfile: #open hidden json file as 'r' read only
            # Reading from json file
            json_object = json.load(openfile)
            integer_counter = 0 # json wasn't happy with json_object["name"][i] because i isn't actually declared an integer or a string
            for i in json_object["users"]: #iterate through the json file
                if json_object["users"][integer_counter]["name"] == self.user_name: #if the self.user_name == a name in the json file 
                    self.json_password = json_object["users"][integer_counter]["password"] # then get the password listed in the json file
                    return self.json_password # return the password in the json file for the correct user
                integer_counter += 1 # keep the counter going
        print(">.< Could not find a database user by that email! Try again :D") # if the user cannot be found then they must try again.
        return self.json_password # returns "0"
        
    def verify_password(self):
        # compares the json_password and the user-inputted password
        password = getpass.getpass(prompt='Password: ', stream=None) # hides password
        if self.json_password == password: #if the passwords are correct
            self.password_correct = True
            return self.password_correct #return a boolean to end the while loop
        else:
            print(">.< Incorrect password! Try Again.")
            self.password_correct = False 
            return self.password_correct #return a boolean to continue the while loop

        
    
        