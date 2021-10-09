from admin import adminActions
from edit_inventory import edit_inventory
from view_inventory import view_inventory
from initialize import initialize_firestore
from interact_inventory import interact
from sign_in import sign_in

class main:
    def __init__(self):
        self.initialize = initialize_firestore()
        self.admin_inventory = edit_inventory()
        self.admin = adminActions()
        self.view_inventory = view_inventory()
        self.interact = interact()
        self.sign_in = sign_in()
    
    def start_file(self):
        #initialize and get user
        db = self.initialize.initialize_firestore()
        user_name = self.sign_in.authenticate_user()
        choice = ""
        while choice != "0":
            print()
            print("0) Exit")
            print("1) Adjust fields")
            print("2) Adjust documents")
            print("3) Display")
            print("4) Create users")
            print("5) Interact")
            choice = input(f"> ")
            print()
            if choice == "1":
                print()
                print("1) Replace Quote")
                print("2) Replace Speaker")
                choice = input(f"> ")
                print()
                if choice == "1":
                    self.admin_inventory.adjust_selected_quote(db)
                elif choice == "2":
                    self.admin_inventory.adjust_selected_speaker(db)
            elif choice == "2":
                print()
                print("1) Add new document")
                print("2) Rename document")
                print("3) Delete document")
                choice = input(f"> ")
                print()
                if choice == "1":  
                    self.admin_inventory.add_new_document(db)
                elif choice == "2":
                    self.admin_inventory.adjust_document_name(db)
                elif choice == "3":
                    self.admin_inventory.delete_selected_document(db)
            elif choice == "3":
                print()
                print("1) Display Users")
                print("2) Display Inventory")
                print("3) Display specific quote")
                choice = input(f"> ")
                print()
                if choice == "1":  
                    self.admin.display_users()
                elif choice == "2":
                    self.view_inventory.display_inventory(db)
                elif choice == "3":
                    self.view_inventory.show_quote(db)
            elif choice == "4":
                self.admin.create_user()
                pass
            elif choice == "5":
                print()
                print("1) Like quote")
                print("2) Comment on quote")
                choice = input(f"> ")
                print()
                if choice == "1":
                    self.interact.update_likes(db)
                elif choice == "2":
                    self.interact.comment(db, user_name)

main().start_file()
    
    #auth.delete_user(uid)
    #print('Successfully deleted user')