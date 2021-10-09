

class view_inventory():

    def display_inventory(self, db):
        results = db.collection("Quotes").get()
        print("")
        print("Search Results:\n---------------\n\n")

        for result in results:
            data = result.to_dict()
            print(
                f"{result.id}\n---------\n{'Quote':<9}{data['Quote']}\n{'Speaker':<9}{data['Speaker']}\n\n"
            )

    def show_quote(self, db):
        name = input("Document name: ")
        result = db.collection("Quotes").document(name).get()
        data = result.to_dict()
        quote = data["Quote"]
        speaker = data["Speaker"]
        print(quote,"\n~ ", speaker)

    