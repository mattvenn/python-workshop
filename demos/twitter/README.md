# Twitter

This demo posts a link to twitter. The account page is: https://twitter.com/piworkshop
It uses a library called Twython.

# Problems

* you can't post duplicate status messages, so including the time is a good way round this
* if you get an error with the default example, there is probably a network restriction like a firewall.

# Useful docs

There are lots of docs about Twython here:

    https://twython.readthedocs.org/en/latest/usage/basic_usage.html

# If you want to create your own account

After you've checked you can tweet with our account you can setup the app to tweet to your own.

It's a bit fiddly, but this worked for me:

* sign up for twitter
* go to https://dev.twitter.com/apps and sign in
* create a new application, the fields don't really matter
* after creating, go to settings and change application type to 'read, write and access direct messages'
* go to the reset keys tab, and click the reset keys button
* go to details tab, and click the 'create my access token' button
* copy the consumer key and secret, and the access token and secret into your program

# Requirements 

the twython module.

For installation instructions see the [Library Readme](../README.md)
