import streamlit as st
import datetime as dt
import pickle as pk

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

with open("./Data/data.dat", "rb") as infile:
    irradiance_df = pk.load(infile)

csv = convert_df(irradiance_df)

if 'sidebartab' not in st.session_state:
    st.session_state.sidebartab = "Overview"

def set_sidebar_tab(sidebar_tab_name):
    st.session_state.sidebartab = sidebar_tab_name

st.title("Solar Generation Report Dashboard")

st.logo("./Data/RepsolLogo.png", link="https://www.repsol.com/es/index.cshtml")

with st.sidebar:
        button1 = st.button("Overview", on_click=set_sidebar_tab, args=["Overview"], key="FryeOverview")
        button2 = st.button("Meterological Data", on_click=set_sidebar_tab, args=["Meterological Data"], key="FryeMet")
        button3 = st.button("PPA Data", on_click=set_sidebar_tab, args=["PPA Data"], key="FryePPA")
        button4 = st.button("ERCOT Settlement Data", on_click=set_sidebar_tab, args=["ERCOT Settlement Data"], key="FryeERCOT")

tab_frye, tab_outpost = st.tabs(["Frye", "Outpost"])

with tab_frye:
    if st.session_state.sidebartab == "Overview":
        st.title("Frye Overview")
        with st.expander("Operating Notes"):
            st.write("This is a place for daily operation notes and other information.")
        analyze_date = st.date_input("Insert Date To View", value=irradiance_df.index.max(), min_value=irradiance_df.index.min(), max_value=irradiance_df.index.max(), format="YYYY-MM-DD", key="FryeDate")
        st.line_chart(irradiance_df.loc[str(analyze_date)], x=None, y="Irradiance")
        st.download_button(label="Download Chart Data As CSV", data=csv, file_name="frye_irradiance.csv", mime="text/csv", key="FryeCSV")   

    if st.session_state.sidebartab == "Meterological Data":
        st.title("Frye Meterological Data")
        st.subheader("Present Met Data Here!")

    if st.session_state.sidebartab == "PPA Data":
        st.title("Frye PPA Data")
        st.subheader("Present PPA Data Here!")

    if st.session_state.sidebartab == "ERCOT Settlement Data":
        st.title("Frye ERCOT Settlement Data")
        st.subheader("Present ERCOT Settlement Data Here!") 

with tab_outpost:
    if st.session_state.sidebartab == "Overview":
        st.title("Outpost Overview")
        with st.expander("Operating Notes"):
            st.write("This is a place for daily operation notes and other information.")
        analyze_date = st.date_input("Insert Date To View", value=irradiance_df.index.max(), min_value=irradiance_df.index.min(), max_value=irradiance_df.index.max(), format="YYYY-MM-DD", key="OutpostDate")
        st.line_chart(irradiance_df.loc[str(analyze_date)], x=None, y="Irradiance")
        st.download_button(label="Download Chart Data As CSV", data=csv, file_name="frye_irradiance.csv", mime="text/csv", key="OutpostCSV")   

    if st.session_state.sidebartab == "Meterological Data":
        st.title("Outpost Meterological Data")
        st.subheader("Present Met Data Here!")

    if st.session_state.sidebartab == "PPA Data":
        st.title("Outpost PPA Data")
        st.subheader("Present PPA Data Here!")

    if st.session_state.sidebartab == "ERCOT Settlement Data":
        st.title("Outpost ERCOT Settlement Data")
        st.subheader("Present ERCOT Settlement Data Here!")