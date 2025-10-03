import requests

url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"

def api_handleing():
    reasponse = requests.get(url)
    data = reasponse.json()
    
    if data["success"] and "data" in data:
        joke = data["data"]["content"]
        return joke
    else:
        raise Exception ("There is Error in Fetching Joke")

def main():
    try:
        joke = api_handleing()
        print("Joke : " , joke)
    except Exception as e:
        print("Error is " , e)
    
if __name__ =="__main__" :
    main()