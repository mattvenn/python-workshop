# flickrapi

Allow us to interact with flickr, specifically we'll use it for uploading photos.

# Authentication

This demo is already setup with an account at:

    http://www.flickr.com/photos/pythonworkshop/

With yahoo login:

    id: pythonworkshop
    password: Pyth0nw0rksh0p

If you want to upload to your own account, you'll need a flickr account, and then to apply for an api key. After logging in, go to this url: http://www.flickr.com/services/api/keys/

You can then apply for a new api key by clicking the 'get another key' button.

When you have your key and secret you can put them into your program. The first time you run your program this part of the code:

(token, frob) = flickr.get_token_part_one(perms='write')
if not token: 
    raw_input("Press ENTER after you authorized this program")

checks if the app has been authenticated yet. If not, your web browser should automatically go to the authenticate page where you can accept the authentication. This will open happen the first time the app is run.

# Documentation

You can read all the docs, and see examples here: http://stuvel.eu/media/flickrapi-docs/documentation/

# Requirements

The flickrapi module has to be installed.

Linux/Mac: use pip
Windows: use win-pip
