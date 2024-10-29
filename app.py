# app.py
from auth import login
from visualization import display_bar_chart

def main():
    print("Welcome to the Application!")
    
    if login():
        print("Access granted. Here’s your dashboard.")
        data = {"Feature A": 20, "Feature B": 15, "Feature C": 10}
        display_bar_chart(data)
    else:
        print("Access denied. Exiting.")

if __name__ == "__main__":
    main()
