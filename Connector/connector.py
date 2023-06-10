import pickle
from pathlib import Path
from bidapp.streamlitdemo.database import fetch_data

def connect(basename):

    creds=  fetch_data(basename)
    
    usernames=[user["key"] for user in creds]
    names=[user["name"] for user in creds]
    hashed_passwords=[user["password"] for user in creds]

    credentials ={"usernames":{}}

    
    for uname,name,pwd in zip(usernames,names,hashed_passwords):
        user_dict={"name":name,"password":pwd}
        credentials["usernames"].update({uname:user_dict})
    
    return credentials