#!/usr/bin/python3
"""
Feature 4: View Insights
Analyzes and summarizes mood logs for trends.
"""

from collections import Counter
from database import connect_db

def view_insights(user_id=1):
    print("\n--- Mood Insights ---")
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT mood FROM moods
        WHERE user_id = ?
        ORDER BY timestamp ASC;
    ''', (user_id,))
    mood_list = [row[0] for row in cursor.fetchall()]
    conn.close()

    if not mood_list:
        print("No mood logs found to analyze.")
        return

    mood_counts = Counter(mood_list)
    most_common = mood_counts.most_common(1)[0]

    print(f"Total moods logged: {len(mood_list)}")
    print(f"Unique moods: {len(mood_counts)}")
    print(f"Most frequent mood: {most_common[0]} ({most_common[1]} times)")

    # Optional: Mood streaks (basic)
    streak = 1
    max_streak = 1
    last_mood = mood_list[0]

    for mood in mood_list[1:]:
        if mood == last_mood:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1
        last_mood = mood

    print(f"Longest same mood streak: {max_streak} days")
