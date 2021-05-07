#Imports and Installs

#conda install -c conda-forge tweepy

import json
from   collections import defaultdict
from   glob import glob
import pandas as pd
import numpy as np
import os
import string
import sys
import tweepy 

try:
    import lzma
except ImportError:
    from backports import lzma
    


# Files and locations
gab_file = os.path.join(sys.path[0], "Documents/gab_twitter/GAB_users.txt")

print(sys.path[0])
print(gab_file)

#Tweepy
#(https://www.geeksforgeeks.org/python-api-lookup_users-in-tweepy/)

# assign the values accordingly 
consumer_key = "Vt31zTtp08E1OgCkJM8ScqWqt" 
consumer_secret = "qE5GYzVS8VTP40GponmSyIrVuEowKqTjDDn5Gh3iY60GuqP21G" 
access_token = "1188495786801278981-Yr27ySCK1enHqe0dfjFsU2MeayfbmN" 
access_token_secret = "FK8xTPkGjOcG4qrcbKiU4VwBlj2cTPL79OSesLPCLVxpa" 
  
# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
  
# calling the api  
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 
  

## Test that this worked! (It does, keep it commented out)

# list of user_ids 
user_ids = [57741058, 4802800777, 1037141442] 
  
# getting the users by user_ids 
users = api.lookup_users(user_ids) 
  
# printing the user details 
for user in users: 
    print("The id by twitter id is : " + str(user.id)) 
    print("The screen name by twitter id is : " + user.screen_name, end = "\n\n")
    
# list of screen_names 
handles = ["geeksforgeeks", "PracticeGfG", "GeeksQuiz"] 
  
# getting the users by screen_names 
users = api.lookup_users(screen_names = handles) 
  
# printing the user details 
for user in users: 
    print("The id by handle is : " + str(user.id)) 
    print("The screen name by handle is : " + user.screen_name, end = "\n\n") 





