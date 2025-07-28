#!/usr/bin/python3
"""
Feature 2: Write Journal Entry
Allows the user to write a reflective journal entry.
"""

from database import connect_db
from datetime import datetime

def write_journal(user_id=1):
    print("\n--- Write Journal Entry ---")
    print("You can reflect on your day here. What made you feel this way?")

    journal_text = input("Enter your journal entry:\n").strip()

    if journal_text:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO entries (user_id, entry, timestamp)
            VALUES (?, ?, ?);
        ''', (user_id, journal_text, datetime.now()))
        conn.commit()
        conn.close()

        print("Your journal entry has been saved.")
    else:
        print("No entry was made. Please try again.")
