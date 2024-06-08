import streamlit as st
import json
import pandas as pd
import numpy as np

st.set_page_config(
   page_title="Web-SEO",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

df = pd.read_json("response.json")

with open('params.json', 'r') as f:
    parameters = json.load(f)

audits = df.lighthouseResult.audits
categories = df.lighthouseResult.categories

add_selectbox = st.sidebar.selectbox(
    "Check View",
    (parameters.keys())
)

webperformance = {"param": [],
                  "score" : [],
                  "Loading Time": []
                  }


st.header("Web Performance")
for param in parameters["Web Performance"]:
    webperformance['param'].append(param)
    webperformance['score'].append(round(audits[param]["score"],2))
    webperformance['Loading Time'].append(round(audits[param]["numericValue"],2))

st.dataframe(webperformance)

st.write(categories)