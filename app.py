import streamlit as st
import pandas as pd

st.set_page_config(page_title="雲端倉庫觀看助手", layout="centered")

# 使用你原本「發布到網路」的 CSV 網址
url = "你的_CSV_網址"

def load_data():
    # 加上時間戳防止緩存
    return pd.read_csv(f"{url}&refresh={pd.Timestamp.now().timestamp()}")

st.title("📊 實時庫存監控")

try:
    df = load_data()
    df.columns = df.columns.str.strip()
    
    st.subheader("目前倉庫庫存")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # 放一個大按鈕，點擊直接打開 Google 表單
    st.subheader("📝 變更庫存")
    form_url = "你的_GOOGLE_表單_連結"
    st.link_button("打開入庫/出庫表單", form_url, use_container_width=True)
    
    st.info("💡 提示：提交表單後，約 1 分鐘後重新整理本網頁即可看到更新。")

except Exception as e:
    st.error(f"資料加載中... 請確保已發布到網路。")




