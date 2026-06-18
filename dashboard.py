import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_autorefresh import (
    st_autorefresh
)

from utils.jira_report import JiraReport


# Page Configuration
st.set_page_config(
    page_title="Jira Metrics Dashboard",
    layout="wide"
)


# Auto Refresh every 10 seconds
st_autorefresh(
    interval=10000,
    key="jira_dashboard_refresh"
)


# Title
st.title(
    "Jira Automation Dashboard"
)


# Load Jira Data
df = JiraReport.generate_report()


if df.empty:

    st.error(
        "No Jira tickets found"
    )

    st.stop()


# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header(
    "Jira Filters"
)


selected_assignee = st.sidebar.selectbox(
    "Select Assignee",
    ["All"] +
    list(df["assignee"].unique())
)


filtered_df = df.copy()


if selected_assignee != "All":

    filtered_df = df[
        df["assignee"] == selected_assignee
    ]


# =========================
# KPI METRICS
# =========================


total_ticket = len(df)


completed = len(
    df[df["status"] == "Done"]
)


in_progress = len(
    df[df["status"] == "In Progress"]
)


todo = len(
    df[df["status"] == "To Do"]
)


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Ticket",
    total_ticket
)


col2.metric(
    "Completed",
    completed
)


col3.metric(
    "In Progress",
    in_progress
)


col4.metric(
    "To Do",
    todo
)


# =========================
# TICKET TABLE
# =========================


st.subheader(
    "Jira Tickets"
)


st.dataframe(
    filtered_df
)


# =========================
# PRIORITY CHART
# =========================


st.subheader(
    "Tickets by Priority"
)


priority_chart = (
    df["priority"]
    .value_counts()
)


st.bar_chart(
    priority_chart
)


# =========================
# STATUS DISTRIBUTION
# =========================


st.subheader(
    "Status Distribution"
)


status_data = (
    df["status"]
    .value_counts()
    .reset_index()
)


status_data.columns = [
    "Status",
    "Count"
]


fig = px.pie(
    status_data,
    names="Status",
    values="Count",
    title="Overall Ticket Status"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =========================
# ASSIGNEE COMPARISON
# =========================


st.subheader(
    "Assignee Workload"
)


assignee_data = (
    df.groupby(
        "assignee"
    )
    .size()
    .reset_index(
        name="Tickets"
    )
)


fig = px.bar(
    assignee_data,
    x="assignee",
    y="Tickets",
    title="Tickets Assigned Per Employee"
)


st.plotly_chart(
    fig,
    use_container_width=True
)