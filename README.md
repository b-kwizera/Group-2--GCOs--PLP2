# Group-2--GCOs--PLP2

# Mood Tracker CLI App

A command-line mood and journaling tracker developed as part of the Peer Learning Project (PLP-2) for BSE Year 1 Trimester 2 at ALU. This tool helps users monitor their emotional well-being through daily mood logging and journaling, offering simple insights into mental health patterns over time.

## Features included in the app

1. **Log Today’s Mood**  
   Users can select their current mood (happy, sad, anxious, calm). The selection is saved with a timestamp to a SQLite database.

2. **Write Journal Entry**  
   Users can reflect on their mood with a prompt or write freely. The entry is stored and linked to the selected mood.

3. **View Mood History**  
   Displays all past moods and journal entries in chronological order.

4. **View Insights**  
   Analyzes frequency of moods (e.g., "You felt calm 4 days in a row").

5. **Menu Navigation with Error Handling**  
   A clean menu interface using numeric selection and validation for invalid inputs.



## Prototype Description

The prototype is a menu-driven Python CLI app.

### How users will interact with it:

- Launch `app.py`
- Choose from menu options (1–5)
- Each selection leads to a clear prompt
- Data is stored in `mood_tracker.db`
- App loops until the user exits



## User Journey Diagram

Start Program
↓
Display Menu
├─ 1 → Log Mood → Save to DB
├─ 2 → Write Journal → Save to DB
├─ 3 → View History → Display from DB
├─ 4 → View Insights → Analyze + Display
└─ 5 → Exit
