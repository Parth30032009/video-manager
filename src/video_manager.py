from constants.constants import format_print

def list_all_videos(cursor):
    videos = cursor.execute("SELECT * FROM videos")
    for row in videos.fetchall():
        id, name, time = row
        format_print(id, name, time)

def add_video(cursor, conn):
    name = input("Name of the video: ")
    time = input("Time of the video: ")
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("\033[33m Video added \033[0m")

def update_video(cursor, conn):
    video_id = input("Enter video id to update: ")
    new_name = input("Enter new name: ")
    new_time = input("Enter new time: ")
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("\033[33m Video Updated \033[0m")

def delete_video(cursor, conn):
    video_id = input("Enter video id to delete: ")
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("\033[33m Video Deleted \033[0m")
