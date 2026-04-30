import streamlit as st
import pandas as pd

st.set_page_config(page_title="雲端倉庫助手", layout="centered")

# 這裡換成你剛才從「發布到網路」複製的 CSV 網址
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTXmWR43c1djcpiFGXqBwFiKu_k92hQPNCaXWoui6HVWlmbM3iOcMRQ2tKmPK6QEuLYdTf8m42Ek7q2/pub?output=csv"

def load_data():
    # 加上一個 random 參數是為了防止網頁快取舊資料
    return pd.read_csv(f"{url}&refresh={pd.Timestamp.now().timestamp()}")

st.title("📱 雲端即時倉庫管理")

try:
    df = load_data()
    # 確保欄位名稱沒有空格
    df.columns = df.columns.str.strip()
    
    st.subheader("目前庫存狀況")
    st.dataframe(df, use_container_width=True, hide_index=True)

    with st.form("update_form"):
        # 這裡的 'ID' 必須跟你 Excel 第一欄的名字一模一樣
        id_list = df['ID'].astype(str).tolist()
        selected_id = st.selectbox("選擇商品 ID", id_list)
        st.info("💡 請直接在 Google Sheets APP 修改數量，網頁重新整理後會自動同步。")
        st.form_submit_button("檢查更新")
            
except Exception as e:
    st.error(f"資料讀取失敗。錯誤訊息: {e}")
    st.write("請檢查 Google 試算表第一列是否為: ID, Name, Quantity")
