import requests
import json

def api_handle():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        userdata = data["data"]
        username = userdata["login"]["username"]
        country = userdata["location"]["country"]
        return username , country
    else :
        raise Exception("Failed to fetch user Data")
    
    
    
def main():
    try:
        username ,country = api_handle()
        print(f"username is {username} and Country is  {country}")
    except Exception as e:
        print("Error in Fetching API : ", str(e))
                
if __name__ == "__main__" :
    main()        
        