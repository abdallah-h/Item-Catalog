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
- Download Vagrant and install.
- Download Virtual Box and install.

## How to run the program
1. Clone [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm).
2. Go to Vagrant directory and clone this repo.
3. Run ```vagrant up``` to start up the VM.
4. Run ```vagrant ssh``` to log into the VM.
5. Run ```cd /vagrant``` to navigate to your vagrant directory.
6. Run ```cd catalog``` to navigate to the app directory.
7. Run ```python database_setup.py``` to load the data and create the tables.
8. Run ```python database_items.py``` to add some data to the database.
9. Run ```python cproject.py``` to run the app.
10. Open your web browser and visit http://localhost:8000/.
11. The app main page will open and you will need to click on login and then use Google+ or Facebook to login.

## Setting up OAuth2.0
### Google OAuth
1. Go to [Google APIs Console](https://console.developers.google.com)
2. Sign in to your account or make a new one.
3. Create a New Project.
4. Choose Credentials from the menu on the left.
5. Choose Web application
6. Enter name 'Catalog Item'
7. Set the authorized JavaScript origins = 'http://localhost:8000'.
8. Set the authorized redirect URIs = 'http://localhost:8000/catalog'.
9. You will then be able to get the client ID and client secret.
10. Copy the client ID and paste it into the `data-clientid` field in login.html file.
11. On the Google APIs Console page download the JSON file and rename it to client_secrets.json.
12. Place the JSON file into catalog directory.

### Facebook OAuth
1. Go to [Facebook Developer](https://developers.facebook.com/)
2. Sign in to your account or make a new one.
3. Click on create new app.
4. Enter name 'Catalog Item'
5. Then select 'Integrate Facebook Login' scenario then confirm.
6. Configure the URL site as: http://localhost:8000/
7. Create a new file and name it fb_client_secrets.json
8. Then copy this code into it
```
{
  "web": {
    "app_id": "PASTE_YOUR_APP_ID_HERE",
    "app_secret": "PASTE_YOUR_CLIENT_SECRET_HERE"
  }
}
```
9. Copy the App ID and App Secret and paste it into 'fb_client_secrets.json' file
10. Place the JSON file into catalog directory.

## JSON endpoints structure

#### Returns JSON format of all catalogs.
```
/catalog.json/
```
#### Returns JSON format of items in a specific catalog.
```
/catalog/<catalog_name>/json/
```
#### Returns JSON format of specific item in a specific catalog.
```
/catalog/<catalog_name>/item/<item_name>/json
```