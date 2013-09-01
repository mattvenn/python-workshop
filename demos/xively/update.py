"""
author: matt venn
"""

#import the cosm library
from CosmFeedUpdate import *

#private key stored in a file
keyfile="api.key"
key=open(keyfile).readlines()[0].strip()

#feed id, this is one I've got ready for the workshop - you'd need to setup your own at cosm.com
feed_id = "120508"
pfu = CosmFeedUpdate(feed_id,key)

#open a special file that stores how long the raspberry has been running for
f=open("/proc/uptime","r");
uptime_string=f.readline()
uptime=uptime_string.split()[0]
pfu.addDatapoint('uptime', uptime)

# finish up and submit the data
pfu.buildUpdate()
pfu.sendUpdate()
print "sent update", uptime
