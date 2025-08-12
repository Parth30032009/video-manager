USER_OPTIONS = {
    1: "List all videos",
    2: "Add a video",
    3: "Update a video",
    4: "Delte a video",
    5: "Show options",
    6: "Exit the app"
}

def format_print(id, name, time):
    # ASCII escape codes for coloured output
    reset = "\033[0m"
    id_color = "\033[34m"
    lable_color = "\033[31m"
    value_color = "\033[35m"
    print(f"{id_color}{id}.{reset} {lable_color}Title:{reset} {value_color}{name}{reset} {lable_color}Duration:{reset} {value_color}{time}{reset}")

