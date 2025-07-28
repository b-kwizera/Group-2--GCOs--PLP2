#!/usr/bin/python3
"""
Feature 3: View Mood History
Displays a chronological list of all mood logs and journal entries.
"""

from database import connect_db

def view_mood_history(user_id=1):
    print("\n--- Mood and Journal History ---")
    conn = connect_db()
    cursor = conn.cursor()

    # Fetch moods
    cursor.execute('''
        SELECT mood, timestamp FROM moods
        WHERE user_id = ?
        ORDER BY timestamp DESC;
    ''', (user_id,))
    mood_logs = cursor.fetchall()

    # Fetch journal entries
    cursor.execute('''
        SELECT entry, timestamp FROM entries
        WHERE user_id = ?
        ORDER BY timestamp DESC;
    ''', (user_id,))
    journal_entries = cursor.fetchall()

    conn.close()

    if not mood_logs and not journal_entries:
        print("No mood or journal history found.")
        return

    print("\n--- Mood Logs ---")
    if mood_logs:
        for mood, date in mood_logs:
            print(f"{date} - Mood: {mood}")
    else:
        print("No mood logs found.")

    print("\n--- Journal Entries ---")
    if journal_entries:
        for entry, date in journal_entries:
            print(f"{date}\nEntry: {entry}\n")
    else:
        print("No journal entries found.")