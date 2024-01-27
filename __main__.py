from .ImageDraw import Paint

def paint_function():
    print("Executing paint function...")
    Paint()

def perform_action():
    user_action = input("What action do you want to perform? ")

    if user_action.lower() == "Draw":
        paint_function()
    else:
        raise ValueError("Invalid action. Only 'Draw' is allowed.")

if __name__ == "__main__":
    try:
        perform_action()
    except ValueError as e:
        print(f"Error: {e}")
