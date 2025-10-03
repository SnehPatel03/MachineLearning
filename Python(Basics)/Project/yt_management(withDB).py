import sqlite3
conn = sqlite3.connect('youtubeList.db') 
cusor = conn.cursor()
cusor.execute('''
              CREATE TABLE IF NOT EXISTS videos (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  time TEXT NOT NULL
              )
             ''')
def list_all_videos():
    cusor.execute('SELECT * FROM videos')
    for row in cusor.fetchall():
          print(
                "Id :" ,row[0], "\n" 
                "Name :", row[1] ,  "\n"  "Time :" ,row[2])
          
def add_video(name,time):
    cusor.execute('INSERT INTO videos (name,time) VALUES (?,?)', (name,time))
    conn.commit()
def update_video(video_id,new_name,new_time):
    cusor.execute('UPDATE videos SET name = ? , time = ? WHERE id=?',(new_name,new_time,video_id))
    conn.commit()
def delete_video(video_id):
    cusor.execute('DELETE FROM  videos where id=?' , (video_id,))
    conn.commit()


def main():
    while(True):
        print("\n YOUTUBE VIDEO MANAGER WITH DB")
        print("1. List All Added Videos.")
        print("2. Add a Youtube Video.")
        print("3. Update the Video.")
        print("4. Delete the Video.")
        print("5. Exist the App.")
        choice = input("Enter a Choice : ")
        
        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name  = input("Enter a Name of Video: ")    
            time  = input("Enter a Time of Video: ")
            add_video(name,time)    
        elif choice == "3":
            list_all_videos()
            video_id = input("Enter a Id of Video to Update: ")
            name = input("Enter a New Name of Video: ")
            time = input("Enter a New Time of Video: ")
            update_video(video_id,name,time)
        elif choice == "4":
            list_all_videos()
            video_id = int(input("Enter a ID of Video to Delete: "))
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("INVALID CHOICE")
    conn.close()
if  __name__ == '__main__':
    main()  