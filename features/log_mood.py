#!/usr/bin/python3
"""
Feature 1: Log Today's Mood
Allows the user to select a mood and save it with a timestamp.
"""

from database import connect_db

MOODS = ["Happy", "Sad", "Anxious", "Calm"]

def log_mood(user_id=1):
    print("\n--- Log Today's Mood ---")
    print("How are you feeling today?")

    for index, mood in enumerate(MOODS, start=1):
        print(f"{index}. {mood}")

    choice = input("Enter the number for your mood: ").strip()

    try:
        mood_index = int(choice) - 1
        if 0 <= mood_index < len(MOODS):
            selected_mood = MOODS[mood_index]

            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO moods (user_id, mood)
                VALUES (?, ?);
            ''', (user_id, selected_mood))
            conn.commit()
            conn.close()

            print(f"Mood '{selected_mood}' logged successfully!")
        else:
            print("Invalid choice. Please select a valid mood number.")
    except ValueError:
        print("Invalid input. Please enter a number.")