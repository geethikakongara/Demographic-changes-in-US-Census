Here's a Python code snippet adapted for the variables you've discussed, formatted for use with Streamlit. This code incorporates mappings and variable names based on the CPS data you provided earlier:

```python
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Define mappings for your specific variables
sex_mapping = {1: 'Male', 2: 'Female'}
income_mapping = {11: "40,000 To 49,999", 15: "100,000 To 149,999", 6: "15,000 To 19,999", 16: "150,000 or More", 
                  2: "5,000 To 7,499", 1: "Less Than $5,000", 13: "60,000 To 74,999", 5: "12,500 To 14,999",
                  14: "75,000 To 99,999", 3: "7,500 To 9,999", 8: "25,000 To 29,999", 9: "30,000 To 34,999", 
                  7: "20,000 To 24,999", 10: "35,000 To 39,999", 12: "50,000 To 59,999", 4: "10,000 To 12,499"}
marital_status_mapping = {7: "Never married", 5: "Divorced", 2: "Married, Armed Forces Spouse Present", 
                          1: "Married, Civilian Spouse Present", -1: "In Universe, Met No Conditions To Assign", 
                          4: "Widowed", 3: "Married, Spouse Absent (exc. Separated)", 6: "Separated"}

# Function to load data from a local file
def load_data():
    df = pd.read_csv('Us_data.csv')
    df.dropna(inplace=True)  # Ensuring no missing values
    df['PESEX'] = df['PESEX'].map(sex_mapping)
    df['HEFAMINC'] = df['HEFAMINC'].map(income_mapping)
    df['PRMARSTA'] = df['PRMARSTA'].map(marital_status_mapping)
    return df

# Check if data is already loaded, if not load it
if 'data' not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

# Streamlit interface
st.title('CPS Data Analysis Dashboard')

if not data.empty:
    # Sidebar for user inputs and filters
    st.sidebar.header("Filter Data")
    gender_to_filter = st.sidebar.multiselect('Select Gender:', options=data['PESEX'].dropna().unique())
    income_to_filter = st.sidebar.multiselect('Select Income Range:', options=data['HEFAMINC'].dropna().unique())
    marital_status_to_filter = st.sidebar.multiselect('Select Marital Status:', options=data['PRMARSTA'].dropna().unique())

    # Applying filters
    if gender_to_filter:
        data = data[data['PESEX'].isin(gender_to_filter)]
    if income_to_filter:
        data = data[data['HEFAMINC'].isin(income_to_filter)]
    if marital_status_to_filter:
        data = data[data['PRMARSTA'].isin(marital_status_to_filter)]

    # Displaying data and statistics
    st.write("### Descriptive Statistics")
    st.write(data.describe())

    # Plots
    st.write("### Gender Distribution")
    fig, ax = plt.subplots()
    data['PESEX'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
    plt.title('Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Frequency')
    st.pyplot(fig)

    st.write("### Income Distribution")
    fig, ax = plt.subplots()
    data['HEFAMINC'].value_counts().plot(kind='bar', color='lightgreen', ax=ax)
    plt.title('Income Distribution')
    plt.xlabel('Income Range')
    plt.ylabel('Frequency')
    st.pyplot(fig)

    st.write("### Marital Status Distribution")
    fig, ax = plt.subplots()
    data['PRMARSTA'].value_counts().plot(kind='bar', color='salmon', ax=ax)
    plt.title('Marital Status Distribution')
    plt.xlabel('Marital Status')
    plt.ylabel('Frequency')
    st.pyplot(fig)
```

This script should give you a functional Streamlit application to analyze and visualize the specified CPS data fields. Adjust the file path and mappings as necessary to fit your actual dataset.
