# Meeting-Task-Assignment-System

Hi, this is a demo of my Meeting Task Assignment System.
This application automatically extracts tasks from meeting audio and assigns them to the correct team members based on skills.

# Upload Audio
Open the Streamlit interface.
Click on “Upload Audio” and select a .wav or .mp3 meeting recording.

The system begins converting speech to text using Whisper.

# View Transcript
The transcript of the meeting appears on the screen.
This helps verify that the speech-to-text step worked correctly.

# Task Extraction
Next, the system extracts tasks using custom logic:
Identifies action verbs like fix, update, design, write
Detects deadlines such as “tomorrow”, “Friday”
Detects priorities such as “critical”, “high”

# Auto Assignment
If a team member is mentioned in the meeting, the system respects that.
Otherwise, it assigns tasks based on matching keywords to skills.

# Final Output
The final structured JSON output is displayed and downloadable.

# Installation & Setup
- Clone the repository
- Create virtual environment
     - python -m venv venv
     - venv/Scripts/activate
- Install dependencies
  pip install -r requirements.txt
- Run the Streamlit app
 streamlit run app.py
