
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def apply_theme(theme):
    if theme == "Dark":
        st.markdown(
            """
            <style>
                body { background-color: #121212; color: #E0E0E0; font-family: 'Arial', sans-serif; }

                /* Sidebar */
                .stSidebar, .css-1d391kg, .css-1v3fvcr { 
                    background-color: #1E1E1E !important; 
                    color: #E0E0E0 !important; 
                }
                
                /* Main Content */
                .stApp { background-color: #181818 !important; }
                .stMarkdown, .stDataFrame, .stTable, .stAlert, .stSelectbox, .stRadio, .stSlider { 
                    color: #E0E0E0 !important; 
                }

                /* Headings & Labels */
                h1, h2, h3, h4, h5, h6 { 
                    font-weight: 800 !important; 
                    font-size: 24px !important; 
                    color: #FFFFFF !important;
                }
                p, label, .stTextInput, .stButton, .stSelectbox label, .stRadio label { 
                    font-weight: 600 !important; 
                    font-size: 16px !important;
                    color: #E0E0E0 !important;
                }

                /* Metric Box */
                div[data-testid="stMetricValue"] { 
                    color: #FFFFFF !important; 
                    font-weight: bold; 
                    font-size: 22px; 
                }
                div[data-testid="stMetricLabel"] { 
                    color: #BDBDBD !important; 
                    font-weight: bold; 
                    font-size: 16px;
                }

                /* Buttons */
                .stButton>button { 
                    background-color: #333333 !important; 
                    color: white !important; 
                    border-radius: 8px; 
                    padding: 10px 18px; 
                    font-size: 16px; 
                    font-weight: 700;
                }

                /* Table & Dataframe Styling */
                .stDataFrame, .stTable { 
                    background-color: #222222 !important; 
                    color: #E0E0E0 !important; 
                    font-size: 16px;
                }

                /* Input fields */
                .stTextInput input, .stNumberInput input, .stSelectbox select {
                    background-color: #333333 !important; 
                    color: #FFFFFF !important; 
                    font-size: 16px; 
                    font-weight: 600;
                    border-radius: 5px;
                    padding: 8px;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    elif theme == "Colorful":
        st.markdown(
            """
            <style>
                body { background: linear-gradient(to right, #6A11CB, #2575FC); color: #1E1E1E; font-family: 'Arial', sans-serif; }

                /* Sidebar */
                .stSidebar, .css-1d391kg, .css-1v3fvcr { 
                    background: linear-gradient(to bottom, #E3F2FD, #BBDEFB) !important; 
                    color: #222222 !important; 
                }

                /* Main Content */
                .stApp { background: linear-gradient(to right, #D9AFD9, #97D9E1) !important; }

                /* Headings & Labels */
                h1, h2, h3, h4, h5, h6 { 
                    font-weight: 800 !important; 
                    font-size: 24px !important; 
                    color: #252A34 !important;
                }
                p, label, .stTextInput, .stButton, .stSelectbox label, .stRadio label { 
                    font-weight: 600 !important; 
                    font-size: 16px !important;
                    color: #252A34 !important;
                }

                /* Metric Box */
                div[data-testid="stMetricValue"] { 
                    color: #4A00E0 !important; 
                    font-weight: bold; 
                    font-size: 22px; 
                }
                div[data-testid="stMetricLabel"] { 
                    color: #222222 !important; 
                    font-weight: bold; 
                    font-size: 16px;
                }

                /* Buttons */
                .stButton>button { 
                    background: linear-gradient(to right, #4A00E0, #8E2DE2); 
                    color: white !important; 
                    border-radius: 8px; 
                    padding: 10px 18px; 
                    font-size: 16px; 
                    font-weight: 700;
                }
                .stButton>button:hover { background: linear-gradient(to right, #8E2DE2, #4A00E0); }

                /* Table & Dataframe Styling */
                .stDataFrame, .stTable { 
                    background: rgba(255, 255, 255, 0.5) !important; 
                    color: #1E1E1E !important;
                    font-size: 16px;
                    backdrop-filter: blur(10px); 
                    border-radius: 10px; 
                    padding: 10px;
                }

                /* Input fields */
                .stTextInput input, .stNumberInput input, .stSelectbox select {
                    background: rgba(255, 255, 255, 0.7) !important; 
                    color: #222222 !important; 
                    font-size: 16px;
                    font-weight: 600;
                    border-radius: 5px;
                    padding: 8px;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    else:  # Light Mode
        st.markdown(
            """
            <style>
                body { background-color: #FFFFFF; color: black; font-family: 'Arial', sans-serif; }

                /* Sidebar */
                .stSidebar, .css-1d391kg, .css-1v3fvcr { background-color: #F5F5F5 !important; color: black !important; }
                
                /* Main Content */
                .stApp { background-color: #FFFFFF !important; }

                /* Headings & Labels */
                h1, h2, h3, h4, h5, h6 { 
                    font-weight: 800 !important; 
                    font-size: 24px !important; 
                    color: #000000 !important;
                }
                p, label, .stTextInput, .stButton, .stSelectbox label, .stRadio label { 
                    font-weight: 600 !important; 
                    font-size: 16px !important;
                    color: #000000 !important;
                }

                /* Metric Box */
                div[data-testid="stMetricValue"] { 
                    color: #000000 !important; 
                    font-weight: bold; 
                    font-size: 22px; 
                }
                div[data-testid="stMetricLabel"] { 
                    color: #333333 !important; 
                    font-weight: bold; 
                    font-size: 16px;
                }

                /* Buttons */
                .stButton>button { 
                    background-color: #007BFF !important; 
                    color: white !important; 
                    border-radius: 8px; 
                    padding: 10px 18px; 
                    font-size: 16px; 
                    font-weight: 700;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )




# Page Configuration
st.set_page_config(
    page_title="Digital Lifestyle Insights",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("D:\\CAI- 2.0\\programing\\dashboard\\socialmedia&entertainment\\filter_dataset_modi.csv")
    return df

df = load_data()
# Apply theme function
def apply_theme(theme):

    if theme == "Dark":
        st.markdown(
            """
            <style>
                /* Background Colors */
                body { background-color: #121212; color: #E0E0E0; }
                .stApp { background-color: #181818; }
                [data-testid="stSidebar"], .css-1d391kg, .css-1v3fvcr { 
                    background-color: #1E1E1E !important; 
                    color: #E0E0E0 !important; 
                }

                /* Headings */
                h1, h2, h3, h4, h5, h6 { 
                    color: #FFFFFF !important; 
                    font-weight: bold !important;
                }

                /* General Text */
                p, li, span, label, div, .stMarkdown { 
                    color: #E0E0E0 !important; 
                    font-weight: 500;
                }

                /* Info, success, warning boxes */
                .stAlert { 
                    background-color: #2c2c2c !important; 
                    color: #E0E0E0 !important; 
                    border-left: 5px solid #1f77b4 !important;
                }

                /* Metric Values */
                div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] { 
                    color: white !important; 
                }

                /* Buttons */
                .stButton>button { 
                    background-color: #333333 !important; 
                    color: #FFFFFF !important; 
                    border: 1px solid #555555 !important;
                    font-weight: bold;
                }
                .stButton>button:hover { 
                    background-color: #555555 !important; 
                }

                /* Inputs */
                .stTextInput input, .stNumberInput input, .stSelectbox select { 
                    background-color: #2c2c2c !important; 
                    color: #FFFFFF !important; 
                    border: 1px solid #555555 !important;
                }

                /* Special Tip/Info Section (optional customization) */
                .stInfo, .stSuccess, .stWarning { 
                    background-color: #2c2c2c !important; 
                    color: #E0E0E0 !important; 
                    border: 1px solid #444 !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Colorful":
        st.markdown(
            """
            <style>
                body { background: linear-gradient(to right, #6A11CB, #2575FC); color: black; }
                .stApp { background: linear-gradient(to right, #D9AFD9, #97D9E1); }
                [data-testid="stSidebar"], .css-1d391kg, .css-1v3fvcr { background: linear-gradient(to bottom, #E3F2FD, #BBDEFB) !important; color: black !important; }
                h1, h2, h3, h4, h5, h6 { color: #252A34; }
                p, label { color: #252A34; }
                div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] { color: #4A00E0 !important; }
                .stButton>button { background: linear-gradient(to right, #4A00E0, #8E2DE2); color: white !important; }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:  # Light theme
        st.markdown(
            """
            <style>
                body { background-color: #FFFFFF; color: black; }
                .stApp { background-color: #FFFFFF; }
                [data-testid="stSidebar"], .css-1d391kg, .css-1v3fvcr { background-color: #F5F5F5 !important; color: black !important; }
                h1, h2, h3, h4, h5, h6 { color: #000000; }
                p, label { color: #000000; }
                div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] { color: black !important; }
                .stButton>button { background-color: #007BFF !important; color: white !important; }
            </style>
            """,
            unsafe_allow_html=True
        )
# Sidebar
with st.sidebar:
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] img {
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 999;
                background-color: white;
                padding: 10px;
                border-bottom: 2px solid #ddd;
            }
            .sidebar-spacer {
                height: 140px;  /* Adjust height based on logo size */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("D:\\CAI- 2.0\\programing\\dashboard\\socialmedia&entertainment\\images.jpg", use_container_width=True)

    st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)

    st.title("📱 Digital Lifestyle Explorer")

    analysis_choice = st.radio(
        "Select Analysis Section:",
        ["🏠 Home Page", "📊 Quick Overview", "👥 User Behavior", "🎮 Entertainment Habits",
         "😴 Well-being Analysis", "💰 Financial Patterns", "🌍 Country-wise Comparison", 
         "📱 Device Preferences"]
    )

    st.markdown("### 📌 Basic Filters")
    age_range = st.slider("Age Range", int(df["Age"].min()), int(df["Age"].max()), (18, 65))
    countries = st.multiselect("Select Countries", options=df["Country"].unique(), default=df["Country"].unique()[:3])

    theme = st.radio("Select Theme", ["Light", "Dark", "Colorful"])

# Apply selected theme
apply_theme(theme)

# Apply filters
filtered_df = df[(df["Age"].between(age_range[0], age_range[1])) & (df["Country"].isin(countries))]

# Page Content Logic
if analysis_choice == "🏠 Home Page":
    st.title("🌐 Welcome to Digital Lifestyle Insights")
    
    st.write("""
        Welcome to **Digital Lifestyle Insights** — your one-stop interactive dashboard to explore how people across the globe spend their digital time, what they watch, how they manage their finances, and even how digital habits impact well-being.
        
        ### 🔍 What You Can Do Here
        - 📊 **Explore Data:** See how digital habits differ across age groups, countries, and devices.
        - 👥 **Understand Behavior:** Analyze trends in social media usage, entertainment preferences, and digital well-being.
        - 🌍 **Compare Countries:** Discover how digital lifestyles differ globally.
        - 🎯 **Personalize Your View:** Use powerful filters to tailor insights to your target audience.

        ### 📌 How to Navigate
        Use the **sidebar** to select the analysis section you’re interested in.  
        Apply filters like **age range**, **country**, and more to focus on the data that matters to you.

        ### 📈 Data Sources
        This dashboard is powered by a comprehensive dataset capturing self-reported digital habits from users across multiple countries, age groups, and device types. It offers a **360-degree view** of modern digital lifestyles.

        ### 🚀 Start Exploring
        Pick a section from the sidebar and dive into the fascinating world of **Digital Lifestyle Insights**.
    """)

    # Optional: Add a few quick stats or fun facts if you want
    st.info("💡 Did you know? Over 70% of users check their phones within 5 minutes of waking up!")

    st.markdown("---")

    st.subheader("📚 Key Sections at a Glance")
    st.write("""
    - **📊 Quick Overview:** High-level summary of digital habits.
    - **👥 User Behavior:** How users engage with social media and entertainment platforms.
    - **🎮 Entertainment Habits:** Streaming, gaming, and content consumption patterns.
    - **😴 Well-being Analysis:** How digital habits influence sleep, stress, and health.
    - **💰 Financial Patterns:** Digital spending, subscriptions, and app purchases.
    - **🌍 Country-wise Comparison:** Compare digital lifestyles across countries.
    - **📱 Device Preferences:** See which devices dominate user habits.
    """)

    st.success("🌟 Tip: Use filters to narrow down insights for specific demographics!")

# Quick Overview
elif analysis_choice == "📊 Quick Overview":
    st.title("Quick Overview of Digital Lifestyle")
    
    # Compute key metrics once
    avg_metrics = filtered_df.agg({
        "Screen Time (hrs)": "mean",
        "Daily Social Media Time (hrs)": "mean",
        "Average Sleep Time (hrs)": "mean",
        "Sleep Quality (scale 1-10)": "mean"
    }).round(1)

    # Display metrics in four columns
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        ("Avg Screen Time", f"{avg_metrics['Screen Time (hrs)']} hrs"),
        ("Avg Social Media", f"{avg_metrics['Daily Social Media Time (hrs)']} hrs"),
        ("Avg Sleep", f"{avg_metrics['Average Sleep Time (hrs)']} hrs"),
        ("Well-being Score", f"{avg_metrics['Sleep Quality (scale 1-10)']}/10")
    ]

    for col, (label, value) in zip([col1, col2, col3, col4], metrics):
        col.metric(label=label, value=value)

    # User selections for analysis
    # User selections for analysis
    category = st.selectbox("Choose category to analyze:", ["Primary Platform", "Age Groups", "Country-wise Comparison", "Device Preferences"])

    # Define plot options dynamically
    if category == "Primary Platform":
        plot_options = ["Bar Chart", "Pie Chart", "Scatter Plot"]  # Custom options for Primary Platform
    elif category == "Age Groups":
        plot_options = ["Bar Chart", "Line Chart", "Scatter Plot"]
    elif category == "Country-wise Comparison":
        plot_options = ["Bar Chart"]
    elif category == "Device Preferences":
        plot_options = ["Bar Chart", "Pie Chart"]
    plot_type = st.selectbox("Select Chart Type:", plot_options)

    # Data processing based on category
    if category == "Age Groups":
        filtered_df["Age Group"] = pd.cut(
            filtered_df["Age"], bins=[0, 20, 30, 40, 50, 60, 100], 
            labels=['0-20', '21-30', '31-40', '41-50', '51-60', '60+']
        )
        plot_data = filtered_df.groupby("Age Group")["Screen Time (hrs)"].mean().reset_index()
        x, y, name_col = "Age Group", "Screen Time (hrs)", None

    elif category == "Country-wise Comparison":
        plot_data = filtered_df.groupby("Country")["Screen Time (hrs)"].mean().reset_index()
        x, y, name_col = "Country", "Screen Time (hrs)", None

    elif category == "Device Preferences":
        plot_data = filtered_df.groupby("Device Type")["Screen Time (hrs)"].mean().reset_index()
        x, y, name_col = "Device Type", "Screen Time (hrs)", "Device Type"

    elif category == "Primary Platform":
        plot_data = filtered_df.groupby("Primary Platform")["Screen Time (hrs)"].sum().reset_index()
        x, y, name_col = "Primary Platform", "Screen Time (hrs)", "Primary Platform"

    # Dynamic Plot Creation
    chart_types = {
        "Bar Chart": px.bar(plot_data, x=x, y=y, title=f"{y} by {x}"),
        "Pie Chart": px.pie(plot_data, names=name_col, values=y, title=f"{y} Distribution"),
        "Scatter Plot": px.scatter(plot_data, x=x, y=y, title=f"{y} vs {x}"),
        "Line Chart": px.line(plot_data, x=x, y=y, title=f"{y} Trend Over {x}") if "Line Chart" in plot_options else None,
        "Box Plot": px.box(filtered_df, x=x, y=y, title=f"Distribution of {y} by {x}") if x in filtered_df and "Box Plot" in plot_options else None
    }

    fig = chart_types.get(plot_type)

    if fig:
        st.plotly_chart(fig, use_container_width=True)
# -------------------------- 👥 USER BEHAVIOR -------------------------- #
elif analysis_choice == "👥 User Behavior":
    st.title("👥 User Behavior Analysis")

    # Compute Key Behavior Metrics (Only for available columns)
    behavior_metrics = {
        "⏳ Avg Social Media Time": (
            round(filtered_df["Daily Social Media Time (hrs)"].mean(), 1)
            if "Daily Social Media Time (hrs)" in filtered_df.columns else None
        ),
        "🎮 Avg Entertainment Time": (
            round(filtered_df["Daily Entertainment Time (hrs)"].mean(), 1)
            if "Daily Entertainment Time (hrs)" in filtered_df.columns else None
        ),
        "💡 Tech Savviness": (
            round(filtered_df["Tech Savviness Level (scale 1-10)"].mean(), 1)
            if "Tech Savviness Level (scale 1-10)" in filtered_df.columns else None
        ),
        "📰 Avg News Consumption Time": (
            round(filtered_df["News Consumption Time (hrs)"].mean(), 1)
            if "News Consumption Time (hrs)" in filtered_df.columns else None
        ),
    }

    # Display Key Metrics (Only non-null values)
    valid_metrics = {k: v for k, v in behavior_metrics.items() if v is not None}

    if valid_metrics:
        st.subheader("📊 Key Behavior Insights")

        # Create columns dynamically
        cols = st.columns(len(valid_metrics))

        for col, (label, value) in zip(cols, valid_metrics.items()):
            with col:
                st.markdown(f"**{label}**")  
                st.write(f"<p style='font-size:22px; font-weight:bold;'>{value} hrs</p>", unsafe_allow_html=True)
    else:
        st.warning("🚨 No relevant behavior metrics found in the dataset.")

    # ----------- User Behavior Insights ----------- #
    category = st.selectbox("Choose behavior category:", 
                            ["Social Media Usage", "Entertainment Habits", "Tech Engagement", "News Consumption"])

    # Define Plot Options
    plot_options = {
        "Social Media Usage": ["Bar Chart", "Pie Chart", "Scatter Plot"],
        "Entertainment Habits": ["Bar Chart", "Line Chart", "Box Plot"],
        "Tech Engagement": ["Scatter Plot", "Line Chart"],
        "News Consumption": ["Bar Chart", "Pie Chart", "Line Chart"]
    }

    plot_type = st.selectbox("Select Chart Type:", plot_options[category])

    # Data Processing Based on Category
    plot_data, x, y, name_col = None, None, None, None

    if category == "Social Media Usage":
        if "Primary Platform" in filtered_df.columns and "Daily Social Media Time (hrs)" in filtered_df.columns:
            plot_data = filtered_df.groupby("Primary Platform")["Daily Social Media Time (hrs)"].mean().reset_index()
            x, y, name_col = "Primary Platform", "Daily Social Media Time (hrs)", "Primary Platform"

    elif category == "Entertainment Habits":
        if "Age" in filtered_df.columns and "Daily Entertainment Time (hrs)" in filtered_df.columns:
            plot_data = filtered_df.groupby("Age")["Daily Entertainment Time (hrs)"].mean().reset_index()
            x, y, name_col = "Age", "Daily Entertainment Time (hrs)", None

    elif category == "Tech Engagement":
        if "Tech Savviness Level (scale 1-10)" in filtered_df.columns and "Daily Social Media Time (hrs)" in filtered_df.columns:
            plot_data = filtered_df.groupby("Tech Savviness Level (scale 1-10)")["Daily Social Media Time (hrs)"].mean().reset_index()
            x, y, name_col = "Tech Savviness Level (scale 1-10)", "Daily Social Media Time (hrs)", None

    elif category == "News Consumption":
        if "Age" in filtered_df.columns and "News Consumption Time (hrs)" in filtered_df.columns:
            # Convert Age into Age Groups for Pie Chart
            filtered_df["Age Group"] = pd.cut(filtered_df["Age"], bins=[0, 18, 30, 50, 100], 
                                              labels=["0-18", "19-30", "31-50", "50+"])
            plot_data = filtered_df.groupby("Age Group")["News Consumption Time (hrs)"].mean().reset_index()
            x, y, name_col = "Age Group", "News Consumption Time (hrs)", "Age Group"

    # Create Plots if Data Exists
    if plot_data is not None and not plot_data.empty:
        chart_types = {
            "Bar Chart": px.bar(plot_data, x=x, y=y, title=f"{y} by {x}"),
            "Pie Chart": px.pie(plot_data, names=name_col, values=y, title=f"Distribution of {y}") if name_col else None,
            "Scatter Plot": px.scatter(plot_data, x=x, y=y, title=f"{y} vs {x}"),
            "Line Chart": px.line(plot_data, x=x, y=y, title=f"{y} Trend Over {x}"),
            "Box Plot": px.box(filtered_df, x=x, y=y, title=f"Distribution of {y} by {x}")
        }

        fig = chart_types.get(plot_type)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Unable to generate the selected chart type.")
    else:
        st.warning("No valid data available for this category.")
# -------------------------- 🎮 ENTERTAINMENT HABITS -------------------------- #
elif analysis_choice == "🎮 Entertainment Habits":
    st.title("🎮 Entertainment Habits Analysis")

    # Ensure DataFrame is not empty
    if filtered_df.empty:
        st.warning("🚨 No data available for analysis.")
    else:
        # Compute Key Entertainment Metrics
        most_popular_platform = (
            filtered_df["Preferred Entertainment Platform"].mode()[0]
            if "Preferred Entertainment Platform" in filtered_df.columns and not filtered_df["Preferred Entertainment Platform"].dropna().empty else "No Data"
        )
        avg_entertainment_time = (
            round(filtered_df["Daily Entertainment Time (hrs)"].mean(), 1)
            if "Daily Entertainment Time (hrs)" in filtered_df.columns and not filtered_df["Daily Entertainment Time (hrs)"].dropna().empty else "No Data"
        )
        avg_spending = (
            round(filtered_df["Monthly Expenditure on Entertainment (USD)"].mean(), 2)
            if "Monthly Expenditure on Entertainment (USD)" in filtered_df.columns and not filtered_df["Monthly Expenditure on Entertainment (USD)"].dropna().empty else "No Data"
        )

        # Display Key Metrics in a Three-Column Layout
        st.subheader("📊 Key Entertainment Insights")

        col1, col2, col3 = st.columns(3)  # Create 3 equal columns

        # Use `st.write()` with Markdown for better alignment
        with col1:
            st.markdown("**🎮 Most Popular Platform**")
            st.write(f"<p style='font-size:24px; font-weight:bold;'>{most_popular_platform}</p>", unsafe_allow_html=True)

        with col2:
            st.markdown("**⏳ Avg Daily Entertainment Time**")
            st.write(f"<p style='font-size:24px; font-weight:bold;'>{avg_entertainment_time} hrs</p>", unsafe_allow_html=True)

        with col3:
            st.markdown("**💰 Avg Monthly Entertainment Spending**")
            st.write(f"<p style='font-size:24px; font-weight:bold;'>${avg_spending}</p>", unsafe_allow_html=True)

        # ----------- Entertainment Behavior Insights ----------- #
        st.subheader("📢 Explore User Entertainment Patterns")
        category = st.selectbox("Choose an entertainment insight:", 
                                ["Most Used Entertainment Platforms",
                                 "Entertainment Time vs Productivity",
                                 "Entertainment Spending Habits"])

        # Define Plot Options
        plot_options = {
            "Most Used Entertainment Platforms": ["Bar Chart", "Pie Chart"],
            "Entertainment Time vs Productivity": ["Scatter Plot", "Line Chart", "Histogram", "Box Plot", "Heatmap"],
            "Entertainment Spending Habits": ["Bar Chart", "Pie Chart"]
        }

        plot_type = st.selectbox("📊 Select Chart Type:", plot_options[category])

        # Data Processing Based on Selection
        plot_data, x, y, name_col = None, None, None, None

        if category == "Most Used Entertainment Platforms":
            if "Preferred Entertainment Platform" in filtered_df.columns and "Daily Entertainment Time (hrs)" in filtered_df.columns:
                plot_data = filtered_df.groupby("Preferred Entertainment Platform")["Daily Entertainment Time (hrs)"].mean().reset_index()
                if not plot_data.empty:
                    x, y, name_col = "Preferred Entertainment Platform", "Daily Entertainment Time (hrs)", "Preferred Entertainment Platform"

        elif category == "Entertainment Time vs Productivity":
            if "Daily Entertainment Time (hrs)" in filtered_df.columns and "Daily Social Media Time (hrs)" in filtered_df.columns:
                plot_data = filtered_df[["Daily Entertainment Time (hrs)", "Daily Social Media Time (hrs)"]].dropna()
                if not plot_data.empty:
                    x, y = "Daily Entertainment Time (hrs)", "Daily Social Media Time (hrs)"

        elif category == "Entertainment Spending Habits":
            if "Preferred Entertainment Platform" in filtered_df.columns and "Monthly Expenditure on Entertainment (USD)" in filtered_df.columns:
                plot_data = filtered_df.groupby("Preferred Entertainment Platform")["Monthly Expenditure on Entertainment (USD)"].mean().reset_index()
                if not plot_data.empty:
                    x, y, name_col = "Preferred Entertainment Platform", "Monthly Expenditure on Entertainment (USD)", "Preferred Entertainment Platform"

        # Create Plots if Data Exists
        if plot_data is not None and not plot_data.empty:
            st.subheader(f"📌 {category} Visualization")

            if category == "Entertainment Time vs Productivity":
                if plot_type == "Scatter Plot":
                    fig = px.scatter(plot_data, x=x, y=y, title=f"{y} vs {x}", color=x, size=y,
                                     color_discrete_sequence=px.colors.qualitative.Vivid)
                    st.plotly_chart(fig, use_container_width=True)

                elif plot_type == "Line Chart":
                    fig = px.line(plot_data, x=x, y=y, title=f"{y} Trend Over {x}", markers=True,
                                  color_discrete_sequence=["#1f77b4"])
                    st.plotly_chart(fig, use_container_width=True)

                elif plot_type == "Histogram":
                    fig = px.histogram(plot_data, x=x, title=f"Distribution of {x}", nbins=20, opacity=0.75)
                    st.plotly_chart(fig, use_container_width=True)

                elif plot_type == "Box Plot":
                    fig = px.box(plot_data, y=x, title=f"Box Plot of {x}", points="all",
                                 color_discrete_sequence=["#636EFA"])
                    st.plotly_chart(fig, use_container_width=True)

                elif plot_type == "Heatmap":
                    # Create a correlation heatmap
                    fig, ax = plt.subplots(figsize=(6, 4))
                    sns.heatmap(plot_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
                    st.pyplot(fig)


            else:
                chart_types = {
                    "Bar Chart": px.bar(plot_data, x=x, y=y, title=f"{y} by {x}", color=x, color_discrete_sequence=px.colors.qualitative.Set2),
                    "Pie Chart": px.pie(plot_data, names=name_col, values=y, title=f"Distribution of {y}", color_discrete_sequence=px.colors.qualitative.Pastel) if name_col else None,
                }
                fig = chart_types.get(plot_type)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Unable to generate the selected chart type.")

        else:
            st.warning("🚨 No valid data available for this category.")

# -------------------------- 😴 WELL-BEING ANALYSIS -------------------------- #
elif analysis_choice == "😴 Well-being Analysis":
    st.title("😴 Well-being Analysis")

    # Ensure DataFrame is not empty
    if filtered_df.empty:
        st.warning("🚨 No data available for analysis.")
    else:
        # Compute Key Well-being Metrics
        well_being_metrics = {
            "Avg Sleep Time (hrs)": (
                f"{round(filtered_df['Average Sleep Time (hrs)'].mean(), 1)} hrs"
                if "Average Sleep Time (hrs)" in filtered_df.columns and not filtered_df["Average Sleep Time (hrs)"].dropna().empty else "No Data"
            ),
            "Avg Screen Time (hrs)": (
                f"{round(filtered_df['Screen Time (hrs)'].mean(), 1)} hrs"
                if "Screen Time (hrs)" in filtered_df.columns and not filtered_df["Screen Time (hrs)"].dropna().empty else "No Data"
            ),
            "Avg Social Isolation Feeling (scale 1-10)": (
                f"{round(filtered_df['Social Isolation Feeling (scale 1-10)'].mean(), 1)} / 10"
                if "Social Isolation Feeling (scale 1-10)" in filtered_df.columns and not filtered_df["Social Isolation Feeling (scale 1-10)"].dropna().empty else "No Data"
            ),
            "Avg Physical Activity Time (hrs)": (
                f"{round(filtered_df['Physical Activity Time (hrs)'].mean(), 1)} hrs"
                if "Physical Activity Time (hrs)" in filtered_df.columns and not filtered_df["Physical Activity Time (hrs)"].dropna().empty else "No Data"
            ),
        }

        # Display Key Metrics in Two Columns
        st.subheader("📊 Key Well-being Insights")
        
        metric_labels = list(well_being_metrics.keys())
        metric_values = list(well_being_metrics.values())

        if any(value != "No Data" for value in well_being_metrics.values()):
            cols = st.columns(2)  # Two-column layout for better readability
            for i in range(0, len(metric_labels), 2):
                for j in range(2):
                    if i + j < len(metric_labels):
                        cols[j].metric(label=metric_labels[i + j], value=metric_values[i + j])
        else:
            st.warning("No relevant well-being metrics found in the dataset.")


        # ----------- Well-being Behavior Insights ----------- #
        st.subheader("📢 Explore Well-being Patterns")
        category = st.selectbox("Choose a well-being insight:", 
                                ["Sleep Patterns",
                                 "Screen Time vs Sleep Quality",
                                 "Social Isolation vs Entertainment",
                                 "Physical Activity vs Sleep Quality"])

        # Define Plot Options
        plot_options = {
            "Sleep Patterns": ["Histogram", "Box Plot"],
            "Screen Time vs Sleep Quality": ["Scatter Plot", "Heatmap"],
            "Social Isolation vs Entertainment": ["Bar Chart"],
            "Physical Activity vs Sleep Quality": ["Line Chart", "Scatter Plot"]
        }

        plot_type = st.selectbox("📊 Select Chart Type:", plot_options[category])

        # Data Processing Based on Selection
        plot_data, x, y = None, None, None

        if category == "Sleep Patterns":
            if "Average Sleep Time (hrs)" in filtered_df.columns:
                plot_data = filtered_df[["Average Sleep Time (hrs)"]].dropna()
                if not plot_data.empty:
                    x = "Average Sleep Time (hrs)"

        elif category == "Screen Time vs Sleep Quality":
            if "Screen Time (hrs)" in filtered_df.columns and "Sleep Quality (scale 1-10)" in filtered_df.columns:
                plot_data = filtered_df[["Screen Time (hrs)", "Sleep Quality (scale 1-10)"]].dropna()
                if not plot_data.empty:
                    x, y = "Screen Time (hrs)", "Sleep Quality (scale 1-10)"

        elif category == "Social Isolation vs Entertainment":
            if "Social Isolation Feeling (scale 1-10)" in filtered_df.columns and "Daily Entertainment Time (hrs)" in filtered_df.columns:
                plot_data = filtered_df[["Social Isolation Feeling (scale 1-10)", "Daily Entertainment Time (hrs)"]].dropna()
                if not plot_data.empty:
                    x, y = "Social Isolation Feeling (scale 1-10)", "Daily Entertainment Time (hrs)"

        elif category == "Physical Activity vs Sleep Quality":
            if "Physical Activity Time (hrs)" in filtered_df.columns and "Sleep Quality (scale 1-10)" in filtered_df.columns:
                plot_data = filtered_df[["Physical Activity Time (hrs)", "Sleep Quality (scale 1-10)"]].dropna()
                if not plot_data.empty:
                    x, y = "Physical Activity Time (hrs)", "Sleep Quality (scale 1-10)"

        # Create Plots if Data Exists
        if plot_data is not None and not plot_data.empty:
            st.subheader(f"📌 {category} Visualization")

            if plot_type == "Scatter Plot":
                fig = px.scatter(plot_data, x=x, y=y, title=f"{y} vs {x}", color=x, size=y,
                                 color_discrete_sequence=px.colors.qualitative.Vivid)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Line Chart":
                fig = px.line(plot_data, x=x, y=y, title=f"{y} Trend Over {x}", markers=True,
                              color_discrete_sequence=["#1f77b4"])
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Histogram":
                fig = px.histogram(plot_data, x=x, title=f"Distribution of {x}", nbins=20, opacity=0.75)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Box Plot":
                fig = px.box(plot_data, y=x, title=f"Box Plot of {x}", points="all",
                             color_discrete_sequence=["#636EFA"])
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Bar Chart":
                fig = px.bar(plot_data, x=x, y=y, title=f"{y} by {x}", color=x, color_discrete_sequence=px.colors.qualitative.Set2)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Heatmap":
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(plot_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
                st.pyplot(fig)

        else:
            st.warning("🚨 No valid data available for this category.")
# -------------------------- 💰 FINANCIAL PATTERNS -------------------------- #
elif analysis_choice == "💰 Financial Patterns":
    st.title("💰 Financial Patterns")

    # Ensure DataFrame is not empty
    if filtered_df.empty:
        st.warning("🚨 No data available for analysis.")
    else:
        # Compute Key Financial Metrics
        financial_metrics = {
            "Avg Monthly Income (USD)": (
                round(filtered_df["Monthly Income (USD)"].mean(), 2)
                if "Monthly Income (USD)" in filtered_df.columns and not filtered_df["Monthly Income (USD)"].dropna().empty else "No Data"
            ),
            "Avg Entertainment Spending (USD)": (
                round(filtered_df["Monthly Expenditure on Entertainment (USD)"].mean(), 2)
                if "Monthly Expenditure on Entertainment (USD)" in filtered_df.columns and not filtered_df["Monthly Expenditure on Entertainment (USD)"].dropna().empty else "No Data"
            ),
            "Avg Time in Online Communities (hrs)": (
                round(filtered_df["Time Spent in Online Communities (hrs)"].mean(), 1)
                if "Time Spent in Online Communities (hrs)" in filtered_df.columns and not filtered_df["Time Spent in Online Communities (hrs)"].dropna().empty else "No Data"
            ),
            "Avg News Consumption Time (hrs)": (
                round(filtered_df["News Consumption Time (hrs)"].mean(), 1)
                if "News Consumption Time (hrs)" in filtered_df.columns and not filtered_df["News Consumption Time (hrs)"].dropna().empty else "No Data"
            ),
        }

        # Display Key Financial Metrics using 2 columns per row
        st.subheader("📊 Key Financial Insights")
        metric_labels = list(financial_metrics.keys())
        metric_values = list(financial_metrics.values())

        if any(value != "No Data" for value in financial_metrics.values()):
            for i in range(0, len(metric_labels), 2):
                cols = st.columns(2)  # Create two columns per row
                for j in range(2):
                    if i + j < len(metric_labels):
                        label = metric_labels[i + j]
                        value = metric_values[i + j]
                        cols[j].metric(label=label, value=f"${value}" if isinstance(value, (int, float)) else value)
        else:
            st.warning("No relevant financial data found in the dataset.")

        # ----------- Financial Behavior Insights ----------- #
        st.subheader("📢 Explore Financial Patterns")
        category = st.selectbox("Choose a financial insight:", 
                                ["Income vs Entertainment Spending",
                                 "News Consumption vs Online Community Engagement",
                                 "Preferred Entertainment Platform Analysis"])

        # Define Plot Options
        plot_options = {
            "Income vs Entertainment Spending": ["Scatter Plot", "Bar Chart"],
            "News Consumption vs Online Community Engagement": ["Scatter Plot", "Line Chart"],
            "Preferred Entertainment Platform Analysis": ["Bar Chart", "Pie Chart"]
        }

        plot_type = st.selectbox("📊 Select Chart Type:", plot_options[category])

        # Data Processing Based on Selection
        plot_data, x, y = None, None, None

        if category == "Income vs Entertainment Spending":
            if "Monthly Income (USD)" in filtered_df.columns and "Monthly Expenditure on Entertainment (USD)" in filtered_df.columns:
                plot_data = filtered_df[["Monthly Income (USD)", "Monthly Expenditure on Entertainment (USD)"]].dropna()
                if not plot_data.empty:
                    x, y = "Monthly Income (USD)", "Monthly Expenditure on Entertainment (USD)"

        elif category == "News Consumption vs Online Community Engagement":
            if "News Consumption Time (hrs)" in filtered_df.columns and "Time Spent in Online Communities (hrs)" in filtered_df.columns:
                plot_data = filtered_df[["News Consumption Time (hrs)", "Time Spent in Online Communities (hrs)"]].dropna()
                if not plot_data.empty:
                    x, y = "News Consumption Time (hrs)", "Time Spent in Online Communities (hrs)"

        elif category == "Preferred Entertainment Platform Analysis":
            if "Preferred Entertainment Platform" in filtered_df.columns:
                plot_data = filtered_df["Preferred Entertainment Platform"].dropna().value_counts().reset_index()
                plot_data.columns = ["Preferred Entertainment Platform", "Count"]
                x, y = "Preferred Entertainment Platform", "Count"

        # Ensure valid plot data before creating plots
        if plot_data is not None and not plot_data.empty:
            st.subheader(f"📌 {category} Visualization")

            if plot_type == "Scatter Plot":
                fig = px.scatter(plot_data, x=x, y=y, title=f"{y} vs {x}", color=x, size=y,
                                 color_discrete_sequence=px.colors.qualitative.Vivid)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Line Chart":
                fig = px.line(plot_data, x=x, y=y, title=f"{y} Trend Over {x}", markers=True,
                              color_discrete_sequence=["#1f77b4"])
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Bar Chart":
                # Convert x-axis column to string to avoid errors
                plot_data[x] = plot_data[x].astype(str)
                fig = px.bar(plot_data, x=x, y=y, title=f"{y} by {x}", color=x, color_discrete_sequence=px.colors.qualitative.Set2)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Pie Chart":
                fig = px.pie(plot_data, names=x, values=y, title="Preferred Entertainment Platform Distribution",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("🚨 No valid data available for this category.")

# -------------------------- 🌍 COUNTRY-WISE COMPARISON -------------------------- #
elif analysis_choice == "🌍 Country-wise Comparison":
    st.title("🌍 Country-wise Comparison")

    # Ensure DataFrame is not empty
    if filtered_df.empty:
        st.warning("🚨 No data available for analysis.")
    else:
        st.subheader("📌 Select a Country for Detailed Insights")

        # Allow user to choose a country
        unique_countries = filtered_df["Country"].dropna().unique()
        selected_country = st.selectbox("Choose a country:", unique_countries)

        # Filter data for the selected country
        country_data = filtered_df[filtered_df["Country"] == selected_country]

        # Compute Key Metrics for Selected Country
        country_metrics = {
            "Avg Monthly Income (USD)": (
                f"${round(country_data['Monthly Income (USD)'].mean(), 2)}"
                if "Monthly Income (USD)" in country_data.columns and not country_data["Monthly Income (USD)"].dropna().empty else "No Data"
            ),
            "Avg Entertainment Spending (USD)": (
                f"${round(country_data['Monthly Expenditure on Entertainment (USD)'].mean(), 2)}"
                if "Monthly Expenditure on Entertainment (USD)" in country_data.columns and not country_data["Monthly Expenditure on Entertainment (USD)"].dropna().empty else "No Data"
            ),
            "Avg Time in Online Communities (hrs)": (
                f"{round(country_data['Time Spent in Online Communities (hrs)'].mean(), 1)} hrs"
                if "Time Spent in Online Communities (hrs)" in country_data.columns and not country_data["Time Spent in Online Communities (hrs)"].dropna().empty else "No Data"
            ),
            "Avg News Consumption Time (hrs)": (
                f"{round(country_data['News Consumption Time (hrs)'].mean(), 1)} hrs"
                if "News Consumption Time (hrs)" in country_data.columns and not country_data["News Consumption Time (hrs)"].dropna().empty else "No Data"
            ),
        }

        # Display Key Metrics in Two Columns
        st.subheader(f"📊 {selected_country} - Financial & Entertainment Metrics")
        cols = st.columns(2)

        for i, (label, value) in enumerate(country_metrics.items()):
            cols[i % 2].metric(label=label, value=value)

        # ----------- Country-wide Comparisons ----------- #
        st.subheader("🌎 Compare Countries on Different Metrics")
        compare_metric = st.selectbox("Select a metric to compare:", [
            "Monthly Income (USD)",
            "Monthly Expenditure on Entertainment (USD)",
            "Time Spent in Online Communities (hrs)",
            "News Consumption Time (hrs)"
        ])

        # Ensure valid data exists for the selected metric
        if compare_metric in filtered_df.columns and not filtered_df[compare_metric].dropna().empty:
            country_comparison = filtered_df.groupby("Country")[compare_metric].mean().reset_index()

            # Create Bar Chart for Country Comparison
            fig = px.bar(
                country_comparison, 
                x="Country", 
                y=compare_metric,
                title=f"Avg {compare_metric} by Country",
                color="Country",
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"No valid data available for {compare_metric}.")

        # ----------- Map Visualization (Optional) ----------- #
        if "Country" in filtered_df.columns:
            st.subheader("🗺️ Geographic Distribution of Monthly Income")

            if "Monthly Income (USD)" in filtered_df.columns and not filtered_df["Monthly Income (USD)"].dropna().empty:
                country_income = filtered_df.groupby("Country")["Monthly Income (USD)"].mean().reset_index()

                # Use Plotly Choropleth Map for Country Income Visualization
                fig = px.choropleth(
                    country_income,
                    locations="Country",
                    locationmode="country names",
                    color="Monthly Income (USD)",
                    hover_name="Country",
                    title="Average Monthly Income by Country",
                    color_continuous_scale=px.colors.sequential.Plasma
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No valid income data available for map visualization.")

# -------------------------- 📱 DEVICE PREFERENCES -------------------------- #
elif analysis_choice == "📱 Device Preferences":
    st.title("📱 Device Preferences")

    # Ensure DataFrame is not empty
    if filtered_df.empty:
        st.warning("🚨 No data available for analysis.")
    else:
        st.subheader("📌 Device Usage Overview")

        # Check if the 'Device Type' column exists and has data
        if "Device Type" in filtered_df.columns and not filtered_df["Device Type"].dropna().empty:
            device_counts = filtered_df["Device Type"].dropna().value_counts().reset_index()
            device_counts.columns = ["Device", "Count"]

            # Display Device Preferences as Metrics
            st.subheader("📊 Most Preferred Devices")
            cols = st.columns(min(len(device_counts), 4))  # Limit columns to max 4 for readability

            for col, row in zip(cols, device_counts.iterrows()):
                col.metric(label=row[1]["Device"], value=f"{row[1]['Count']} Users")

            # ----------- Device Preference Visualizations ----------- #
            st.subheader("📢 Explore Device Preferences")
            plot_type = st.selectbox("📊 Select Chart Type:", ["Bar Chart", "Pie Chart"])

            # Generate Device Preference Charts
            if plot_type == "Bar Chart":
                fig = px.bar(device_counts, x="Device", y="Count", 
                             title="Device Preferences", 
                             color="Device", 
                             color_discrete_sequence=px.colors.qualitative.Set2)
                st.plotly_chart(fig, use_container_width=True)

            elif plot_type == "Pie Chart":
                fig = px.pie(device_counts, names="Device", values="Count",
                             title="Device Preference Distribution",
                             color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("🚨 No valid data available for device preferences.")

        # ----------- Cross-Analysis: Device vs. Screen Time ----------- #
        st.subheader("📊 Device Usage by Screen Time")

        # Check if necessary columns exist and have data
        if all(col in filtered_df.columns and not filtered_df[col].dropna().empty for col in ["Device Type", "Screen Time (hrs)"]):
            screen_time_data = filtered_df.groupby("Device Type")["Screen Time (hrs)"].mean().reset_index()

            fig = px.bar(screen_time_data, x="Device Type", y="Screen Time (hrs)", 
                         title="Average Daily Screen Time by Device",
                         color="Device Type",
                         color_discrete_sequence=px.colors.qualitative.Vivid)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("🚨 Required columns missing or no valid screen time data for comparison.")
