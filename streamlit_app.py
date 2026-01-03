import streamlit as st
import pandas as pd

st.set_page_config(page_title="T9A – Test Filters", layout="centered")
st.title("The Ninth Age – Filters test")

@st.cache_data
def load_data():
    return pd.read_csv("data/sample_stats.csv")

df = load_data()

armies = st.multiselect(
    "Leger",
    sorted(df["army"].unique()),
    default=sorted(df["army"].unique())
)

versions = st.multiselect(
    "Versie",
    sorted(df["version"].unique()),
    default=sorted(df["version"].unique())
)

filtered = df[
    df["army"].isin(armies) &
    df["version"].isin(versions)
]

if filtered.empty:
    st.warning("Geen data voor deze selectie.")
else:
    avg_winrate = filtered["wins"].sum() / filtered["games"].sum()
    st.metric("Average winrate", f"{avg_winrate:.1%}")
    st.dataframe(filtered)
