import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st. set_page_config(layout="wide")
# Data
match_data = [
    {"Date": "2024-01-15", "Goals": 1, "Assists": 0, "Passes_Attempted": 50, "Passes_Completed": 45, "Dribbles_Attempted": 10, "Dribbles_Completed": 7, "Tackles": 5, "Interceptions": 3, "Match_Rating": 7.8},
    {"Date": "2024-01-22", "Goals": 0, "Assists": 1, "Passes_Attempted": 55, "Passes_Completed": 50, "Dribbles_Attempted": 8, "Dribbles_Completed": 6, "Tackles": 6, "Interceptions": 4, "Match_Rating": 7.5},
    {"Date": "2024-02-01", "Goals": 2, "Assists": 0, "Passes_Attempted": 48, "Passes_Completed": 42, "Dribbles_Attempted": 12, "Dribbles_Completed": 9, "Tackles": 7, "Interceptions": 2, "Match_Rating": 8.2},
    {"Date": "2024-02-15", "Goals": 1, "Assists": 1, "Passes_Attempted": 53, "Passes_Completed": 47, "Dribbles_Attempted": 11, "Dribbles_Completed": 8, "Tackles": 5, "Interceptions": 3, "Match_Rating": 8.0},
    {"Date": "2024-02-22", "Goals": 0, "Assists": 2, "Passes_Attempted": 52, "Passes_Completed": 48, "Dribbles_Attempted": 9, "Dribbles_Completed": 6, "Tackles": 4, "Interceptions": 3, "Match_Rating": 7.6},
    {"Date": "2024-03-01", "Goals": 2, "Assists": 0, "Passes_Attempted": 50, "Passes_Completed": 44, "Dribbles_Attempted": 10, "Dribbles_Completed": 7, "Tackles": 6, "Interceptions": 4, "Match_Rating": 8.1},
]

training_data = [
    {"Date": "2024-01-15", "Distance_Covered_km": 9.5, "Sprint_Speed_kmh": 27.8, "Recovery_Time_min": 1.8},
    {"Date": "2024-01-22", "Distance_Covered_km": 10.0, "Sprint_Speed_kmh": 28.2, "Recovery_Time_min": 1.6},
    {"Date": "2024-02-01", "Distance_Covered_km": 9.8, "Sprint_Speed_kmh": 27.5, "Recovery_Time_min": 1.7},
    {"Date": "2024-02-15", "Distance_Covered_km": 10.2, "Sprint_Speed_kmh": 28.0, "Recovery_Time_min": 1.5},
    {"Date": "2024-02-22", "Distance_Covered_km": 9.9, "Sprint_Speed_kmh": 27.9, "Recovery_Time_min": 1.7},
    {"Date": "2024-03-01", "Distance_Covered_km": 10.1, "Sprint_Speed_kmh": 28.1, "Recovery_Time_min": 1.6},
]

biometric_data = [
    {"Date": "2024-01-15", "Height_cm": 178, "Weight_kg": 70, "Body_Fat_pct": 12, "Muscle_Mass_kg": 35, "Resting_Heart_Rate_bpm": 60},
    {"Date": "2024-02-01", "Height_cm": 178, "Weight_kg": 71, "Body_Fat_pct": 11.8, "Muscle_Mass_kg": 36, "Resting_Heart_Rate_bpm": 59},
    {"Date": "2024-02-15", "Height_cm": 178, "Weight_kg": 71, "Body_Fat_pct": 11.6, "Muscle_Mass_kg": 36, "Resting_Heart_Rate_bpm": 58},
    {"Date": "2024-03-01", "Height_cm": 178, "Weight_kg": 71.5, "Body_Fat_pct": 11.5, "Muscle_Mass_kg": 36.5, "Resting_Heart_Rate_bpm": 58},
]

scouting_reports = [
    {"Date": "2024-01-15", "Work_Ethic": 8, "Game_Intelligence": 9, "Adaptability": 7, "Notes": "Excellent positioning and vision"},
    {"Date": "2024-02-01", "Work_Ethic": 9, "Game_Intelligence": 8, "Adaptability": 8, "Notes": "Strong leadership on the field"},
    {"Date": "2024-02-15", "Work_Ethic": 8, "Game_Intelligence": 8, "Adaptability": 9, "Notes": "Consistent and reliable under pressure"},
    {"Date": "2024-03-01", "Work_Ethic": 9, "Game_Intelligence": 9, "Adaptability": 8, "Notes": "Great team player and strategist"},
]

# Convert data to DataFrame
match_df = pd.DataFrame(match_data)
training_df = pd.DataFrame(training_data)
biometric_df = pd.DataFrame(biometric_data)
scouting_df = pd.DataFrame(scouting_reports)

player_profile = {
    "Name": "Chika Onwuanibe",
    "Age": 19,
    "Position": "Striker",
    "Team": "Gospel Oak Football Club / Hammersmith FC"
}

# Streamlit App
st.title("Chika Onwuanibe - Player Performance Dashboard")

# Display Player Profile
st.header("Player Profile")
st.write(f"**Name:** {player_profile['Name']}")
st.write(f"**Age:** {player_profile['Age']}")
st.write(f"**Position:** {player_profile['Position']}")
st.write(f"**Team:** {player_profile['Team']}")

# Set Date column to datetime
match_df['Date'] = pd.to_datetime(match_df['Date'])
training_df['Date'] = pd.to_datetime(training_df['Date'])
biometric_df['Date'] = pd.to_datetime(biometric_df['Date'])
scouting_df['Date'] = pd.to_datetime(scouting_df['Date'])

# Streamlit App
st.title("Player Performance Dashboard")


# Technical Skills
st.header("Technical Skills Analysis")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Passing Accuracy Over Time")
    match_df['Passing_Accuracy'] = match_df['Passes_Completed'] / match_df['Passes_Attempted'] * 100
    fig, ax = plt.subplots()
    sns.lineplot(data=match_df, x='Date', y='Passing_Accuracy', ax=ax)
    ax.set_ylabel('Passing Accuracy (%)')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
    
with col2:
    st.subheader("Dribbling Success Rate")
    match_df['Dribbling_Success_Rate'] = match_df['Dribbles_Completed'] / match_df['Dribbles_Attempted'] * 100
    fig, ax = plt.subplots()
    sns.barplot(data=match_df, x='Date', y='Dribbling_Success_Rate', ax=ax)
    ax.set_ylabel('Dribbling Success Rate (%)')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
    
with col3:
    st.subheader("Shooting Conversion Rate")
    fig, ax = plt.subplots()
    sns.barplot(data=match_df, x='Date', y='Goals', ax=ax)
    ax.set_ylabel('Goals')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)

# Physical Attributes
st.header("Physical Attributes Analysis")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Tackles Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=match_df, x='Date', y='Tackles', ax=ax)
    ax.set_ylabel('Tackles')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
    
with col2:
    st.subheader("Interceptions Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=match_df, x='Date', y='Interceptions', ax=ax)
    ax.set_ylabel('Interceptions')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
    
with col3:
    st.subheader("Match Rating Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(data=match_df, x='Date', y='Match_Rating', ax=ax)
    ax.set_ylabel('Match Rating')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
# Tactical Understanding
st.header("Tactical Understanding Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Positioning on the Field")
    # Example: heatmap of tackles and interceptions
    fig, ax = plt.subplots()
    sns.heatmap(match_df.pivot_table(values='Match_Rating', index='Tackles', columns='Interceptions'), ax=ax)
    ax.set_ylabel('Tackles')
    ax.set_xlabel('Interceptions')
    st.pyplot(fig)
    
with col2:
    st.subheader("Decision-Making Metrics")
    fig, ax = plt.subplots()
    sns.lineplot(data=match_df, x='Date', y='Match_Rating', ax=ax)
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    ax.set_ylabel('Match Rating')
    st.pyplot(fig)

# Psychological Factors
st.header("Psychological Factors Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Training Session Effort Ratings")
    fig, ax = plt.subplots()
    sns.lineplot(data=scouting_df, x='Date', y='Work_Ethic', ax=ax, label='Work Ethic')
    sns.lineplot(data=scouting_df, x='Date', y='Game_Intelligence', ax=ax, label='Game Intelligence')
    sns.lineplot(data=scouting_df, x='Date', y='Adaptability', ax=ax, label='Adaptability')
    ax.set_ylabel('Rating (1-10)')
    ax.set_xticklabels(labels=match_df['Date'], rotation=90)
    st.pyplot(fig)
    
with col2:
    st.subheader("Performance in Different Positions")
    # Example: performance notes summary
    for i, row in scouting_df.iterrows():
        st.write(f"Date: {row['Date'].date()}")
        st.write(f"Notes: {row['Notes']}")
        st.write(" ")

# Summary and Recommendations
st.header("Summary and Recommendations")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Overall Performance Rating")
    st.metric(label="Average Match Rating", value=f"{match_df['Match_Rating'].mean():.2f}")
    
with col2:
    st.subheader("Strengths and Areas for Improvement")
    strengths = """
    - Excellent passing accuracy
    - Strong tactical understanding
    - High work ethic and game intelligence
    """
    improvements = """
    - Improve shooting conversion rate
    - Enhance dribbling success under pressure
    """
    st.write("**Strengths**")
    st.write(strengths)
    st.write("**Areas for Improvement**")
    st.write(improvements)

st.subheader("Development Plan")
development_plan = """
- Focus on shooting drills and techniques to improve conversion rate
- Dribbling practice in high-pressure scenarios
- Continued physical conditioning and stamina building
"""
st.write(development_plan)

st.subheader("Projected Market Value Growth")
fig, ax = plt.subplots()
sns.lineplot(data=match_df, x='Date', y='Match_Rating', ax=ax)
ax.set_ylabel('Projected Market Value')
ax.set_xticklabels(labels=match_df['Date'], rotation=90)
st.pyplot(fig)

st.subheader("Injury Risk and Preventive Measures")
st.write("Monitoring biometric data shows low injury risk with current preventive measures in place.")
