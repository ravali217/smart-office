from datetime import datetime

def current_time():

    now = datetime.now()

    return now.strftime(
        "%d-%m-%Y %H:%M:%S"
    )


if __name__ == "__main__":

    print(
        "Current Date and Time:",
        current_time()
    )