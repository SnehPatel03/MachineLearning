import json

def main():
    def load_data():
        try:
            with open('youtube.txt','r') as file:
                return json.load(file)
        except FileNotFoundError:
            return [2,2]   
            
    def save_data_helper(videos):
        with open('youtube.txt','w') as file:
            json.dump(videos, file)
            
    def list_all_videos(videos):
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} ({video['time']})")
                
    def add_video(videos):
        name = input("Enter a Video Name: ")
        time = input("Enter a Video Time: ")
        videos.append({"name": name, "time": time})
        save_data_helper(videos)
        print("Video added successfully!")
        
    def update_video(videos):
        list_all_videos(videos)
        index = int(input("Enter the number of Video to Update Details: "))
        if 1<= index <=len(videos):
              name = input("Enter a new Video Name: ")
              time = input("Enter a new Video Time: ")
              videos[index-1] = {"name":name , "time":time}
              save_data_helper(videos)
        else:
            print("Invalid Index to update.")    
    def delete_video(videos):
        list_all_videos(videos)
        index = int(input("Enter the Number of video to delete."))
        if 1<=index<=len(videos):
            del(videos[index-1])
            save_data_helper(videos)
            print("Video Deleted Successfully")
        else:
            print("Invalid Index to update.")    

    while True:
        videos = load_data()
        print("\n=== Youtube Manager ===")
        print("1. List all Videos")
        print("2. Add a Youtube Video")
        print("3. Update Youtube details")
        print("4. Delete a Youtube Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Please enter a valid choice.")

if __name__ == '__main__':
    main()
