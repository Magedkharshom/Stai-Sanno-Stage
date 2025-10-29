import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os # To check if plot files exist

# --- Page Configuration (Set Title and Icon) ---
# This should be the first Streamlit command
st.set_page_config(page_title="Stai Sano Event Analysis", page_icon="📊")

# --- Load Data ---
# Use a function with caching to load data only once
@st.cache_data # Decorator to cache the data
def load_data(filepath):
    try:
        df = pd.read_csv(filepath, encoding='utf-8-sig')
        return df
    except FileNotFoundError:
        st.error(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

DATA_FILE = "ANALYSIS_READY_SATISFACTION.csv"
df_satisfaction = load_data(DATA_FILE)

# --- Title and Introduction ---
st.title("📊 Stai Sano Event Satisfaction Analysis")
st.markdown("""
Welcome to the analysis dashboard for the Stai Sano event satisfaction surveys.
Use this app to explore the results.
""")

# --- Display Data (Optional) ---
if df_satisfaction is not None:
    st.header("Cleaned Survey Data Sample")
    st.dataframe(df_satisfaction.head())

    st.markdown("---") # Visual separator

    # --- Display Plots ---
    st.header("Exploratory Data Analysis Plots")

    # Plot 1: Satisfaction by Event
    plot1_path = 'plot1_satisfaction_by_event.png'
    if os.path.exists(plot1_path):
        st.subheader("Average Satisfaction per Event")
        st.image(plot1_path, caption='Events ranked by average overall satisfaction score.')
    else:
        st.warning(f"Plot file not found: {plot1_path}")

    # Plot 2: Satisfaction by Category
    plot2_path = 'plot2_satisfaction_by_category.png'
    if os.path.exists(plot2_path):
        st.subheader("Average Satisfaction per Topic Category")
        st.image(plot2_path, caption='Topic categories ranked by average overall satisfaction score.')
    else:
        st.warning(f"Plot file not found: {plot2_path}")

    # Add other plots similarly...
    # plot5_path = 'plot5_metric_pairplot.png'
    # if os.path.exists(plot5_path):
    #     st.subheader("Relationship Between Metrics")
    #     st.image(plot5_path, caption='Correlations between Overall Satisfaction, Clarity, and Usefulness.')

    # plot6_path = 'plot6_feature_importance.png'
    # if os.path.exists(plot6_path):
    #     st.subheader("ML Model: Feature Importance")
    #     st.image(plot6_path, caption='Factors predicting overall satisfaction according to the Random Forest model.')

else:
    st.warning("Could not load data to display.")

st.markdown("---")
st.info("End of Dashboard")