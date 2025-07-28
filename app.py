#!/usr/bin/python3
"""
Main application runner for the Mood Tracker CLI app.
Provides a menu-driven interface for the user.
"""

from features.log_mood import log_mood
from features.write_journal import write_journal
from features.view_history import view_mood_history
from features.view_insights import view_insights

def display_menu():
    print("\n=== Mood Tracker CLI ===")
    print("1. Log Today's Mood")
    print("2. Write Journal Entry")
    print("3. View Mood History")
    print("4. View Insights")
    print("5. Exit")

def main():
    user_id = 1  # assuming single user for simplicity

    while True:
        display_menu()
        choice = input("Choose an option (1–5): ").strip()

        if choice == '1':
            log_mood(user_id)
        elif choice == '2':
            write_journal(user_id)
        elif choice == '3':
            view_mood_history(user_id)
        elif choice == '4':
            view_insights(user_id)
        elif choice == '5':
            print("Goodbye! See you tomorrow.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
