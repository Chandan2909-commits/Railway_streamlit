import streamlit as st
import pyautogui as p
import time as t
from datetime import datetime
import threading

st.title("🚂 Train Ticket Booking")

# Input form
with st.form("booking_form"):
    from_location = st.text_input("From where you want to book a ticket?", placeholder="e.g., New Delhi")
    to_location = st.text_input("Where you want to go today?", placeholder="e.g., Mumbai")
    date = st.date_input("Enter the date of travel", min_value=datetime.today())
    
    col1, col2 = st.columns(2)
    
    with col1:
        manual_search = st.form_submit_button("Manual Search")
    with col2:
        auto_search = st.form_submit_button("Auto Search (PyAutoGUI)")
    
    if manual_search or auto_search:
        if from_location and to_location:
            formatted_date = date.strftime("%d-%m-%Y")
            
            if manual_search:
                st.success(f"Searching trains from **{from_location}** to **{to_location}** on **{formatted_date}**")
                irctc_url = f"https://www.irctc.co.in/nget/train-search?from={from_location}&to={to_location}&date={formatted_date}"
                st.markdown(f"[🔗 Open IRCTC Website]({irctc_url})")
                st.info("Click the link above to proceed with booking on IRCTC website")
            
            elif auto_search:
                st.warning("⚠️ Automation will start in 5 seconds. Make sure your browser is ready!")
                
                def run_automation():
                    t.sleep(5)
                    p.hotkey('ctrl', 't')
                    p.write("https://www.irctc.co.in/nget/train-search")
                    p.press('enter')
                    t.sleep(10)
                    p.moveTo(959, 890)
                    t.sleep(1)
                    p.leftClick()
                    p.moveTo(323, 507)
                    t.sleep(1)
                    p.leftClick()
                    p.write(from_location)
                    t.sleep(1)
                    p.moveTo(263, 596)
                    p.leftClick()
                    t.sleep(1)
                    p.moveTo(263, 596)
                    t.sleep(1)
                    p.leftClick()
                    p.write(to_location)
                    t.sleep(1)
                    p.moveTo(153, 626)
                    t.sleep(1)
                    p.leftClick()
                    t.sleep(1)
                    p.moveTo(263, 685)
                    t.sleep(1)
                    p.leftClick()
                    p.write(formatted_date)
                    t.sleep(1)
                    p.moveTo(789, 517)
                    t.sleep(1)
                    p.leftClick()
                    p.hotkey('ctrl', 'a')
                    t.sleep(1)
                    p.press('delete')
                    t.sleep(1)
                    p.write(formatted_date)
                    t.sleep(1)
                    p.moveTo(224, 815)
                    t.sleep(1)
                    p.leftClick()
                
                threading.Thread(target=run_automation, daemon=True).start()
                st.success("🤖 Automation started! Check your browser.")
        else:
            st.error("Please fill in both From and To locations")
