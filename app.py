import streamlit as st
import pandas as pd

# 頁面設定
st.set_page_config(page_title="實時庫存監控", page_icon="📊")

# --- 這裡填入你發布到網路的 CSV 網址 ---
# 記得要在 Google 試算表選：檔案 > 共用 > 發布到網路 > 選擇 CSV 格式
CSV_URL = "你的_CSV_網址_填在這裡"

# --- 這裡填入你的 Google 表單連結 ---
FORM_URL = "你的_GOOGLE_表單連結_填在這裡"

def load_data():
    # 加上隨機參數防止手機瀏覽器讀取舊快取
    try:
        data = pd.read_csv(f"{CSV_URL}&t={pd.Timestamp.now().timestamp()}")
        data.columns = data.columns.str.strip()
        return data
    except:
        return None

st.title("📊 實時庫存監控")

df = load_data()

if df is not None:
    # 顯示精美的表格
    st.subheader("目前倉庫庫存")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # 登記操作按鈕
    st.subheader("📦 登記出入貨")
    st.write("點擊下方按鈕填寫表單，完成後重新整理此頁面。")
    st.link_button("👉 打開登記表單", FORM_URL, use_container_width=True)
    
    if st.button("🔄 刷新數據"):
        st.rerun()

else:
    st.error("⚠️ 無法讀取資料。請確認 Google 試算表已『發布到網路』並選擇 CSV 格式。")
    st.info("目前的 CSV 網址是否正確？")
