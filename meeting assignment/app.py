import streamlit as st
from logic.speech_to_text import convert_audio_to_text
from logic.task_extractor import detect_tasks
from logic.assignment_logic import load_team, assign_tasks
import json

st.title("🎙️ Meeting Task Assignment System")

uploaded_file = st.file_uploader("Upload meeting audio", type=["mp3","wav","m4a"])

if uploaded_file:
    st.info("Converting audio → text...")
    text = convert_audio_to_text(uploaded_file)
    st.write("### Transcript:")
    st.write(text)

    st.info("Extracting tasks...")
    tasks = detect_tasks(text)

    st.info("Assigning tasks...")
    team = load_team()
    final_tasks = assign_tasks(tasks, team)

    st.success("Task Extraction Complete")

    st.write("### 📌 Final Output")
    st.json(final_tasks)

    # download JSON
    st.download_button("Download JSON", json.dumps(final_tasks, indent=4),
                       file_name="tasks.json")
