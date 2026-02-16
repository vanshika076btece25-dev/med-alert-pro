import streamlit as st
import json
import time
from datetime import datetime

st.set_page_config(page_title="Med-Alert Pro", page_icon="💊")

# --- INITIALIZE SESSION STATE ---
if 'registered' not in st.session_state:
    st.session_state.registered = False

# --- PATIENT REGISTRATION (First Screen) ---
if not st.session_state.registered:
    st.title("🏥 Patient Registration")
    st.write("Welcome! Please enter your details to start receiving WhatsApp alerts.")
    
    with st.form("reg_form"):
        name = st.text_input("Patient Name")
        # Yahan hum WhatsApp number mang rahe hain
        phone = st.text_input("WhatsApp Number (with country code)", placeholder="+919876543210")
        
        if st.form_submit_button("Start Dashboard"):
            if name and phone:
                # Save details to a file for the background service to read
                user_info = {"name": name, "phone": phone}
                with open("user_data.json", "w") as f:
                    json.dump(user_info, f)
                
                st.session_state.registered = True
                st.rerun()
            else:
                st.error("Please fill all details!")

# --- MAIN DASHBOARD (Second Screen) ---
else:
    st.title("💊 Medication Roadmap")
    
    # Show current patient info
    with open("user_data.json", "r") as f:
        user = json.load(f)
    st.success(f"Logged in as: {user['name']} | Alerts active on: {user['phone']}")

    # --- ADD MEDICINE SECTION ---
    with st.sidebar:
        st.header("➕ Add Medicine")
        m_name = st.text_input("Medicine Name")
        m_time = st.time_input("Reminder Time")
        
        if st.button("Save Schedule"):
            new_med = {"name": m_name, "time": m_time.strftime("%H:%M"), "status": "Pending"}
            try:
                with open("med_data.json", "r") as f: data = json.load(f)
            except: data = []
            data.append(new_med)
            with open("med_data.json", "w") as f: json.dump(data, f)
            st.success("Saved! Your WhatsApp will ring at this time.")

    # --- ROADMAP VIEW ---
    st.subheader("🛣️ Today's Journey")
    try:
        with open("med_data.json", "r") as f: meds = json.load(f)
        for m in meds:
            st.info(f"⏰ {m['time']} - **{m['name']}**")
    except:
        st.write("No medicines added yet.")