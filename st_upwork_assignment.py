import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Mock setup: Replace with df = pd.read_csv("your_file.csv")
df = pd.read_csv("c:\\Users\\CEO-KCB\\logistics_data.csv")
today = datetime.now()

st.title("📦 Logistics Query MVP")
query = st.text_input("Ask a logistics question:").lower()

if query:
    # 1. Late Items
    if "late" in query:
        late_df = df[pd.to_datetime(df['Forecast_Arrival']) < today]
        st.write("Current Late Items:", late_df)

    # 2. Required next 30 days
    elif "30 days" in query:
        next_30 = today + timedelta(days=30)
        req_df = df[pd.to_datetime(df['Required_Date']).between(today, next_30) & df['Received_Date'].isna()]
        st.write("Items required within 30 days (Unreceived):", req_df)

    # 3. Status of Item X (Extracts the last word as Item ID)
    elif "status of item" in query:
        item_id = query.split()[-1].upper()
        status = df[df['Item_ID'] == item_id]['Status'].values
        st.info(f"Status of {item_id}: {status[0] if len(status)>0 else 'Not Found'}")

    # 4. Workpack X Counts
    elif "workpack" in query:
        wp_id = query.split()[-1].upper()
        counts = df[df['Workpack'] == wp_id]['Status'].value_counts()
        st.bar_chart(counts)

    # 5. Variance
    elif "variance" in query:
        variance_df = df[df['Forecast_Arrival'] != df['Received_Date']]
        st.write("Items with Date Variance:", variance_df)
    
    else:
        st.warning("Warning : Asked query is out of scope. Please ask about late items, next 30 days, status of item X, workpack X counts, or variance.")