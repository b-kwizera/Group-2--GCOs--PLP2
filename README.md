Mood Tracker CLI App
Group-2 – GCOs – PLP2

A command-line mood and journaling tracker developed as part of the Peer Learning Project (PLP-2) for BSE Year 1, Trimester 2 at the African Leadership University (ALU). This application enables users to track their emotional well-being by logging daily moods and journal entries, offering helpful insights into mental health trends over time.

📌 Features
Log Today’s Mood

Select your current mood (e.g., happy, sad, anxious, calm)

Mood is saved with a timestamp in a SQLite database

Write Journal Entry

Reflect on your day using a guided prompt or free-write

Journal entries are linked to the logged mood and stored securely

View Mood History

Review all past moods and journal entries

Displays data in chronological order

View Insights

Get automatic analysis of mood trends

E.g., “You felt calm 4 days in a row”

Menu Navigation with Error Handling

Intuitive CLI menu with numbered options

Validates user input and handles errors gracefully

🚀 Getting Started
Prerequisites
Python 3.x installed on your machine

SQLite (comes bundled with Python’s sqlite3 module)

Installation
1. Clone the repository:

git clone https://github.com/your-username/mood-tracker-cli.git
cd mood-tracker-cli

2. Install any required dependencies (if applicable):

pip install -r requirements.txt

Run the App

python3 app.py

🧭 User Flow

Start Program
     ↓
Display Main Menu
 ├─ 1. Log Mood        → Save mood with timestamp
 ├─ 2. Write Journal   → Save entry linked to mood
 ├─ 3. View History    → Show all entries chronologically
 ├─ 4. View Insights   → Analyze mood trends
 └─ 5. Exit            → End session

📂 Data Storage
All mood logs and journal entries are stored locally using SQLite (mood_tracker.db), ensuring offline functionality and data privacy.

🤝 Contributing
This project was created collaboratively by Group 2 as part of the PLP-2 Coding Lab. Contributions for future improvements are welcome via pull requests.

📧 Contact
For questions or suggestions, feel free to reach out to any member of Group 2 or your PLP facilitator.

