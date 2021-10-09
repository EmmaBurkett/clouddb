class view_inventory():

    def display_inventory(self, db):
        #get all documents from database
        results = db.collection("Quotes").get()
        #pretty formatting
        print("")
        print("Search Results:\n---------------\n\n")

        #print all docuemtns in pretty formatting
        for result in results:
            data = result.to_dict() #get's the field for each document
            print(
                f"{result.id}\n---------\n{'Quote':<9}{data['Quote']}\n{'Speaker':<9}{data['Speaker']}\n\n"# <9 puts them all on the same line - same as C language logic
            ) #prints each field except likes the comment collections

    def show_quote(self, db):
        #get document name and fields
        name = input("Document name: ")
        result = db.collection("Quotes").document(name).get()
        data = result.to_dict()
        #display
        quote = data["Quote"]
        speaker = data["Speaker"]
        print(quote,"\n~ ", speaker)

    