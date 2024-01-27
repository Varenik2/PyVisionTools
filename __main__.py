from .ImageDraw import Paint

def paint_function():
    print("Executing paint function...")
    Paint()

def perform_action():
    user_action = input("What action do you want to perform? ")
    Paint()

    if user_action.lower() == "Draw":
        paint_function()

if __name__ == "__main__":
    perform_action()
