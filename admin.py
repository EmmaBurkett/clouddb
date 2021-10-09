from firebase_admin import auth
import json
import getpass
class adminActions():
    def create_user(self):
        name = input("Last, and First Name: " )
        email = input("Email: ")
        password = getpass.getpass(prompt="Ultra-Secret-Password: ", stream=None)
        if len(password) < 6:
            print("Password must be longer than 5 characters")
            self.create_user()
        #is_admin = input("Admin Status? (True/False) ")

        # Data to be written
        record_password ={
            "name" : str(name),
            "password": str(password)
        }
        filename = "clouddb\passwords.json"
        with open(filename, 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["users"].append(record_password)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

        user = auth.create_user(
        email= email,
        password = password,
        display_name= name)
        print('Sucessfully created new user: {0}'.format(user.uid))
        # whoops KXPoN20XIXVJb7xfjKqQ0r7KIpx1
        # cNvmWuHkveNpHxt9QzjsG3dC37X2 Hello4

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
            print(f'User: {user.display_name}, {user.uid}')

    
