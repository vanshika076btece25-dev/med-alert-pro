import streamlit as st
import json
import os
import subprocess

# 1. Backend service ko auto-start karne ke liye
if "service_started" not in st.session_state:
    subprocess.Popen(["python", "med_service.py"])
    st.session_state["service_started"] = True

# 2. Multi-user Dashboard logic
def load_data(phone):
    filename = f"data_{phone}.json" # Har user ki alag file
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

# Baki login logic mein phone number use karke data load karein
       
        
