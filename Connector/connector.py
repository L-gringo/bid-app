import pickle
from pathlib import Path

def connect():
        
    names=["NOUMON Emmanuel", "ALIOU Mahmoulh"]
    usernames=["Mannoufreaky","l-gringo"]
    #passwords=[""]
    credentials ={"usernames":{}}

    
    file_path=Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords=pickle.load(file)
        
    for uname,name,pwd in zip(usernames,names,hashed_passwords):
        user_dict={"name":name,"password":pwd}
        credentials["usernames"].update({uname:user_dict})
    
    return credentials