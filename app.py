# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10nuoMHLNf_SgLmpcfB-3Xksorpywgv9h
"""

#python code
# Import streamlit for the web app
import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

# Custom CSS to create vertical lines
st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 90%;
    }
    .vl {
        border-left: 2px solid black;
        height: 500px;
        position: absolute;
        left: 50%;
        margin-left: -3px;
        top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the dashboard, centered
st.title('US Senator Portfolio Analysis Dashboard', anchor='center')

# Using columns to create a two-column layout for the top charts, and adding vertical lines
col1, col2 = st.columns(2)

# First column for the portfolio value evolution
with col1:
    st.header("Overall Senators' Portfolio Evolution", anchor='center')
    # Placeholder for the portfolio value chart
    portfolio_value_chart_placeholder = st.empty()

# Vertical line
st.markdown('<div class="vl"></div>', unsafe_allow_html=True)

# Second column for the CO2 emissions evolution
with col2:
    st.header("Overall CO2 Emissions in the US", anchor='center')
    # Placeholder for the CO2 emissions chart
    co2_emissions_chart_placeholder = st.empty()

# Horizontal line
st.markdown('---')  # This creates a horizontal line in Streamlit

# Using columns to create a two-column layout for the bottom sections
col3, col4 = st.columns(2)

# Third column for the ranking of top polluting companies
with col3:
    st.header("Stock Analysis: Pollution Index vs Popularity", anchor='center')
    # Placeholder for the polluting companies table
    polluting_companies_table_placeholder = st.empty()

# Vertical line
st.markdown('<div class="vl"></div>', unsafe_allow_html=True)

# Fourth column for the AI-generated information
with col4:
    st.header("AI Generated Info on Selected Stock", anchor='center')
    # Placeholder for the AI-generated information
    ai_generated_info_placeholder = st.empty()
