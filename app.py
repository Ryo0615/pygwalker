import pandas as pd
import pygwalker as pyg
import streamlit as st

# Set page config
st.set_page_config(
    page_title="PygWalker Demo",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 以下をサイドバーに表示
st.sidebar.markdown("### csvファイルを入力してください")
# ファイルアップロード
uploaded_files = st.sidebar.file_uploader(
    "Choose a CSV file", accept_multiple_files=False
)

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    pyg.walk(df, env="Streamlit", dark="light", show_cloud_tool=True)
else:
    st.write("表示するデータがありません")
