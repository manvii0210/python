import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Dashboard')

df = sns.load_dataset('titanic')
pd.DataFrame(df)
