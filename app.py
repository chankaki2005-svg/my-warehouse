import streamlit as st
from st_files_connection import FilesConnection
import pandas as pd

st.set_page_config(page_title="雲端倉庫助手", layout="centered")

# 這裡填入你的 Google Sheet 網址 (需公開編輯權限)
url = "你的_GOOGLE_SHEET_完整網址"

def load_data():
    # 讀取雲端資料
    return pd.read_csv(url.replace('/edit?usp=sharing', '/export?format=csv'))

st.title("📱 雲端即時倉庫管理")

try:
    df = load_data()
    
    # 顯示目前庫存
    st.subheader("目前庫存狀況")
    st.dataframe(df, use_container_width=True, hide_index=True)

    # 快速出入庫操作
    with st.form("update_form"):
        selected_id = st.selectbox("選擇商品 ID", df['ID'].tolist())
        mode = st.radio("操作類型", ["入庫 (+)", "出庫 (-)"], horizontal=True)
        amount = st.number_input("數量", min_value=1, step=1)
        submit = st.form_submit_button("提交更改")

        if submit:
            st.info("💡 提示：在網頁版直接修改 Google Sheets 需搭配 API，初步建議直接在手機打開 Google Sheets APP 修改最快，或透過 Streamlit 串接 API 實現全自動。")
            
except Exception as e:
    st.error("請確認 Google Sheet 網址正確且已開啟『知道連結的人皆可編輯』權限")
