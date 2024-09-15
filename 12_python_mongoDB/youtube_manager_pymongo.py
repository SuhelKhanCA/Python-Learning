from pymongo import MongoClient


client = MongoClient("mongodb+srv://<======>:<=======>@cluster0.xabmu.mongodb.net/youtube-todo", tlsAllowInvalidCertificates=True) # not a good practice to include id password in code file
# tlsAllowInvalidCertificates=True # Not a good practice

db = client["youtube-todo"]
print(client)

video_collections = db["videos"]

print(video_collections)

def add_video(name, time):
    video_collections.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collections.update_one({"_id":video_id}, {"$set":{"name": name, "time": time}})


def display_video():
    for video in video_collections.find({}):
        print(f"ID: {video['_id']}, Name : {video['name']}, and Time: {video['time']}")


def delete_video(video_id):
    video_collections.delete_one({"_id": video_id})
    # TODO : debug this video_id problem


def main():

    while True:
        print("\n==============Youtube Manager =============\n")
        print("1. Add Video")
        print("2. Delete Video")
        print("3. Update Video")
        print("4. Display Video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case "2":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "3":
                video_id  = input("Enter the video ID to update")
                name  = input("Enter the new video name")
                timem  = input("Enter the new video time")
                update_video(video_id, name, time)
            case "4":
                display_video()
            case "5":
                break
            case _:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()