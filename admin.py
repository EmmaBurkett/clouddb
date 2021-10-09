from firebase_admin import auth
import json
import getpass
class adminActions():
    def create_user(self):
        #get user input
        name = input("Last, and First Name: " )
        email = input("Email: ")
        password = getpass.getpass(prompt="Ultra-Secret-Password: ", stream=None) # hides password
        if len(password) < 6: #makes sure password is up to snuff
            print("Password must be longer than 5 characters")
            self.create_user()
        #is_admin = input("Admin Status? (True/False) ")

        #put email and password into a json file!
        # Preps data for .gitignore json file
        record_password ={
            "name" : str(name),
            "password": str(password)
        }

        filename = "clouddb\passwords.json"
        with open(filename, 'r+') as file: #r+ lets you write to a file without overwritting everything and even sets up the correct commas and all that
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside json["users"]
            file_data["users"].append(record_password)
            # Sets file's current position at offset.
            file.seek(0)
            # converts data to json.
            json.dump(file_data, file, indent = 4)
        
        #put information into the Firestore!
        user = auth.create_user(
        email= email,
        password = password,
        display_name= name)
        print('Sucessfully created new user: {0}'.format(user.uid)) # outputs unique id for user

    def display_users(self):
        '''page = auth.list_users()
        while page:
            for user in page.users:
                print('User: ' + user.uid)
            # Get next batch of users.
            page = page.get_next_page()'''

        # Iterate through all users. This will still retrieve users in batches,
        # buffering no more than 1000 users in memory at a time.
        for user in auth.list_users().iterate_all():
            print(f'User: {user.display_name}, {user.uid}') #this will display all the users

    
