# Item Catalog
## Introduction
Create a Item Catalog app where users can add, edit, and delete Catalogs and Items in the Catalogs.

## Skills used for this project
- Python
- HTML
- CSS
- Bootstrap
- JQuery
- Ajax
- Flask
- SQLAchemy
- OAuth
- Facebook / Google Login

## System setup
1. Download Vagrant and install.
2. Download Virtual Box and install.
3. Clone this repository.

## setting up OAuth2.0
- You will need to sign up for a google account and set up a client id and secret.
- You Can also signup for facebook account and set up the client id and secret.

## how to run the program
1. Run ```vagrant up``` to start up the VM.
2. Run ```vagrant ssh``` to log into the VM.
3. Run ```cd /vagrant``` to change to your vagrant directory.
4. Run ```cd catalog``` to change to the app directory.
5. Run ```python database_setup.py``` to load the data and create the tables.
6. Run ```python database_items.py``` to add some data to the database.
7. Run ```python cproject.py``` to run the app.
8. Open your web browser and visit http://localhost:8000/.
9. The app main page will open and you will need to click on login and then use Google+ or Facebook to login.

