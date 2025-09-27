import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("clinical_trial.csv")

# Title
st.title("Clinical Trial Dashboard")

# Show data
st.subheader("Raw Data")
st.dataframe(data)

# Bar chart: Response Rate
st.subheader("Response Rate Comparison")
fig1, ax1 = plt.subplots()
ax1.bar(x=data["Group"], height=data["Response Rate (%)"], color=["green", "gray"])
ax1.set_ylabel("Response Rate (%)")
ax1.set_ylim(0, 100)
st.pyplot(fig1)

# Bar chart: Side Effects
st.subheader("Side Effects Comparison")
fig2, ax2 = plt.subplots()
ax2.bar(x=data["Group"], height=data["Side Effects (%)"], color=["red", "gray"])
ax2.set_ylabel("Side Effects (%)")
ax2.set_ylim(0, 100)
st.pyplot(fig2)
