import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("D:\\CAI- 2.0\\programing\\dashboard\\socialmedia&entertainment\\filtered_dataset.csv")  # Replace with your actual dataset path

# Sidebar - Filters and Settings
st.sidebar.header("Filter Options")
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (18, 40))
gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique(), default=df["Gender"].unique())
country = st.sidebar.multiselect("Select Country", df["Country"].unique(), default=df["Country"].unique())
occupation = st.sidebar.multiselect("Select Occupation", df["Occupation"].unique(), default=df["Occupation"].unique())
income_range = st.sidebar.slider("Monthly Income (USD)", int(df["Monthly Income (USD)"].min()), int(df["Monthly Income (USD)"].max()), (1000, 5000))

# Apply Filters
df_filtered = df[(df["Age"].between(*age_range)) & (df["Gender"].isin(gender)) & (df["Country"].isin(country)) & (df["Occupation"].isin(occupation)) & (df["Monthly Income (USD)"].between(*income_range))]

# Sidebar - Plot Selection
st.sidebar.header("Visualization Options")
plot_type = st.sidebar.selectbox("Select Plot Type", ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Correlation Heatmap"])
variable_x = st.sidebar.selectbox("Select X-axis Variable", df.columns)
variable_y = st.sidebar.selectbox("Select Y-axis Variable", df.columns)

# Main Dashboard Title
st.title("📊 Social Media & Entertainment Dashboard")
st.write("This dashboard provides insights into digital habits, screen time, and online activities.")

# Visualization Based on User Selection
st.subheader("📈 Data Visualization")

if plot_type == "Bar Chart":
    fig, ax = plt.subplots()
    sns.barplot(data=df_filtered, x=variable_x, y=variable_y, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif plot_type == "Line Chart":
    fig, ax = plt.subplots()
    sns.lineplot(data=df_filtered, x=variable_x, y=variable_y, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif plot_type == "Scatter Plot":
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_filtered, x=variable_x, y=variable_y, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif plot_type == "Pie Chart":
    fig, ax = plt.subplots()
    df_filtered[variable_x].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)

elif plot_type == "Correlation Heatmap":
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df_filtered.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

# Display Key Statistics
st.subheader("📊 Key Statistics")
st.write("- **Average Screen Time:**", df_filtered["Screen Time (hrs)"].mean(), "hrs/day")
st.write("- **Average Social Media Fatigue Level:**", df_filtered["Social Media Fatigue Level (scale 1-10)"].mean())
st.write("- **Average Sleep Time:**", df_filtered["Average Sleep Time (hrs)"].mean(), "hrs/night")
st.write("- **Most Popular Platform:**", df_filtered["Primary Platform"].mode()[0])

# Display Filtered Data Table
st.subheader("📋 Filtered Data Table")
st.dataframe(df_filtered)
