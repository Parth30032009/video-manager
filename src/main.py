import sys
import os
from constants.constants import USER_OPTIONS
from db import get_connection
from video_manager import list_all_videos, add_video, update_video, delete_video

def show_options(options):
    for key, value in options.items():
        print(f"{key}. {value}")

def main():
    conn, cursor = get_connection()
    os.system("clear")
    print("Youtube Video Manager")
    show_options(USER_OPTIONS)

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                list_all_videos(cursor)
            case 2:
                add_video(cursor, conn)
            case 3:
                update_video(cursor, conn)
            case 4:
                delete_video(cursor, conn)
            case 5:
                show_options(USER_OPTIONS)
            case 6:
                conn.close()
                os.system("clear")
                print("Program exited")
                sys.exit()
            case _:
                print("Invalid choice. Try again")

if __name__ == "__main__":
    main()
