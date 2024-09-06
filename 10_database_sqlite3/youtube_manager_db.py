import sqlite3

conn = sqlite3.connect("YT_videos.db")

cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
 ''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id=?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(id):
    cur.execute("DELETE FROM videos WHERE id=?", (id,))
    conn.commit()


def main():
    
    while True:
        print("\n Youtube Manager with DB | Choose an option")
        print("1. List all favorite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                print("\n List of all favorite videos:")
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(id, name, time)
            case '4':
                id = input("Enter video ID to delete: ")
                delete_video(id)
            case '5':
                break
            case _:
                print("\n Invalid choice. Please choose a valid option.")

    conn.close()

if __name__ == "__main__":
    main()