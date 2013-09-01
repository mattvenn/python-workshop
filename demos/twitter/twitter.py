from twython import Twython
#twython installs with win-pip
import os
from datetime import datetime

#this demo posts tweets from piworkshop (https://twitter.com/piworkshop)

#authenticate, check the README.md for how to set up your own account
twitter = Twython(
    #consumer key
    "fF86BdSdopE9FAES5UNgPw",
    #consumer secret
    "n7G4K80kYQ6NDMQiYn3GY5Hyk82fF2So17Nl1UQdGWE",
    #access_token
    "1336977176-4CgpPJnJBx7kCRqnwLcRbXI3nLpHj44sp3r2bXy",
    #access_token_secret
    "5rLNvZm3JZdkx0K1Jx9jgsqMG6MmGLAQmPdJ7ChtzA",
)

#make the tweet
time = datetime.now()
link = "http://www.flickr.com/photos/pythonworkshop/9599102000"
message = "%s posted at %s" % (link, time)

#post it
print "sending a text tweet:", message
twitter.update_status(status=message)
print "sent"

