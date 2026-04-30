import streamlit as st
from st_files_connection import FilesConnection
import pandas as pd
from datetime import datetime

# 設定頁面
st.set_page_config(page_title="專業雲端倉庫系統", layout="centered")

# --- 設定區 (請填入你的資訊) ---
SHEET_ID = "你的_GOOGLE_SHEET_ID_填在這裡"
# 這裡使用 Google Apps Script 或直接導向 CSV 讀取 (目前先維持讀取，寫入建議透過 Google API)
url_stock = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=stock"

def load_data():
    df = pd.read_csv(url_stock)
    df.columns = df.columns.str.strip()
    return df

st.title("📦 倉庫即時管理 (含日期紀錄)")

try:
    df = load_data()
    st.subheader("📊 目前庫存清單")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()

    # --- 出入庫操作區 ---
    st.subheader("🔄 出入庫操作")
    with st.form("action_form"):
        target_id = st.selectbox("選擇商品 ID", df['ID'].astype(str).tolist())
        mode = st.radio("動作", ["入庫 (+)", "出庫 (-)"], horizontal=True)
        amount = st.number_input("變動數量", min_value=1, step=1)
        
        st.write("⚠️ **注意**：點擊下方按鈕後，請手動點擊出現的連結以確認更新（因為安全限制，網頁直接修改 Excel 需設定私密 API）。")
        
        if st.form_submit_button("產生更新連結"):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 這裡提供一個快速跳轉連結，讓你可以直接在手機跳到試算表修改，或是透過 API 達成
            st.success(f"已準備好處理 {target_id} 的{mode}。")
            st.info(f"操作時間：{now}")
            # 這是最簡單的「半自動」方法，點擊後跳轉到 Google Sheet 進行編輯
            sheet_link = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit"
            st.markdown(f"[點我打開表格進行快速修改]({sheet_link})")

except Exception as e:
    st.error(f"連線異常: {e}")
