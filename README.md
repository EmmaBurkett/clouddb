# Overview

My main goal in creating this was to understand cloud databases and obtain a proficient level of knowledge in it. I didn't have too much of a plan for what the end result would be because I didn't know anything about cloud databases.

My program is a database of quotes - you can remove quotes, replace quotes, replace the speaker, comment on a quote, like a quote, display all documents, and display a specific quote by the document's name. Some other functions that were supposed to be reserved for admin only is to rename, add, and delete a document, display the created user accounts, create a user account.

The purpose for writing this was to gain a basic understanding of cloud databases, and a sufficient pool of resources on the topic so that I can learn more on my own - without outside help.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

I am using Firestore's free cloud database.

Collection -> Documents -> 1) Fields and 2) Collection -> Document -> Fields
Quotes -> Quote One.. Two... Three.. etc. -> 1) Fields Quote, Speaker, and likes 2) Comments -> Unique ID for Documents -> Fields Comment Title, Comment, Submitted by (anon or signed in user), Submitted at (time).
Some documents don't have the comments collection after it because that is auto-generated when the user adds a comment. If there is already a comment collection the program will not create another collection but will add another document with the comments fields.

# Development Environment

* Firestore/Firebase(https://console.firebase.google.com/u/0/project/hello-world-plus-my-files-lol/firestore/data/~2FQuotes~2FQuote%20Five~2FComments~2FkCse6l087M5Qh9c7tRdb)
* Visual Studio Code
* Python 3.9.6
## Libraries used:
* import firebase_admin
* from   firebase_admin import credentials - utilizes the auto-generated json file from firestore
* from   firebase_admin import firestore - finds my files on firestore
* from   firebase_admin import auth - finds people with access to the database and their corresponding information (this allowed the sign in function at the start of the program)
* import json - let's python interact with a json file
* import getpass - hides passwords

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Firestore/Firebase](https://firebase.google.com/)
* [Slack](https://stackoverflow.com/)


# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Ability to view the comments
* Admin privileges to specific users only
* Admin should be able to delete comments
* Timestamps for every action listing specifically what was changed and who did it (except for anonymous comment posting)
* Document names in the quote collection auto generated in this format Quote 1, Quote 2, Quote 3, Quote 4 etc.
* Remove Speaker
* Display all quotes, comments, and likes (IF THERE ARE ANY COMMENTS AND LIKES 0.o) - not sure how to do this but I could figure it out!
