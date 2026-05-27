import streamlit as st
import pandas as pd
import plotly.express as px
import os
import file_utils
from styles import apply_custom_css
apply_custom_css()

if not st.session_state.get('authentication_status'):
    st.warning("🔒 กรุณาเข้าสู่ระบบที่หน้าหลัก (app.py) ก่อนใช้งานครับ")
    st.stop()

username = st.session_state['username']

st.markdown("<h2 style='color: #4A90E2;'>📊 สถิติและการใช้งานของคุณ</h2>", unsafe_allow_html=True)

df = file_utils.get_stats(username)
total_files = df["Count"].sum() if not df.empty else 0

if not df.empty and total_files > 0:
    most_common = df.loc[df['Count'].idxmax()]['Category']
    most_common_count = df.loc[df['Count'].idxmax()]['Count']
else:
    most_common = "-"
    most_common_count = 0

m1, m2, m3 = st.columns(3)
m1.metric("📦 ไฟล์ในระบบทั้งหมด", f"{total_files} ไฟล์")
m2.metric("🏆 หมวดหมู่ยอดฮิต", most_common, f"{most_common_count} รายการ")
m3.metric("👤 สถานะผู้ใช้", username.capitalize(), "Online ✅")

st.divider() 

if not df.empty and total_files > 0:
    fig = px.pie(df, values='Count', names='Category', hole=0.4, 
                 title="สัดส่วนการเก็บไฟล์แยกตามโฟลเดอร์",
                 color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)
    st.table(df)
else:
    st.info("ยังไม่มีข้อมูลสถิติ กรุณาจัดการไฟล์เพื่อแสดงผล")

st.divider() 
st.subheader("🕒 ประวัติการทำงานล่าสุด")

log_df = file_utils.get_activity_log(username)

if not log_df.empty:
    st.dataframe(
        log_df, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Time": st.column_config.TextColumn("📅 วัน-เวลา"),
            "Filename": st.column_config.TextColumn("📄 ชื่อไฟล์"),
            "Category": st.column_config.TextColumn("📂 หมวดหมู่/ที่อยู่"),
            "Status": st.column_config.TextColumn("✅ สถานะ")
        }
    )
    
    # --- 🌟 ส่วนที่เพิ่มใหม่ Day 9: Export Data & Stats ---
    st.write("📥 **ส่งออกและจัดการข้อมูล**")
    csv_data = log_df.to_csv(index=False).encode('utf-8-sig') # ใช้ utf-8-sig เพื่อรองรับภาษาไทยใน Excel
    
    col_btn1, col_btn2 = st.columns([2, 1])
    
    with col_btn1:
        st.download_button(
            label="📊 ดาวน์โหลดประวัติเป็นไฟล์ CSV (Excel)",
            data=csv_data,
            file_name=f"Activity_Report_{username}_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            help="คลิกเพื่อโหลดข้อมูลไปเปิดใน Microsoft Excel หรือ Google Sheets"
        )
        
    with col_btn2:
        if st.button("🗑️ ล้างประวัติการทำงาน"):
            log_path = f"Users/{username}/activity_log.csv"
            if os.path.exists(log_path):
                os.remove(log_path)
                st.success("ล้างประวัติเรียบร้อยแล้ว")
                st.rerun()

    # กล่องวิเคราะห์สถิติ (พับเก็บได้)
    with st.expander("📈 วิเคราะห์สถิติเบื้องต้นของไฟล์ (คลิกเพื่อดูรายละเอียด)"):
        c1, c2 = st.columns(2)
        with c1:
            top_cat = log_df['Category'].mode()[0] if not log_df['Category'].empty else "-"
            st.write(f"หมวดหมู่ที่ใช้งานบ่อยสุด: **{top_cat}**")
        with c2:
            temp_df = log_df.copy()
            temp_df['Date'] = pd.to_datetime(temp_df['Time']).dt.date
            avg_actions = temp_df.groupby('Date').size().mean()
            st.write(f"เฉลี่ยการจัดการไฟล์: **{avg_actions:.1f} รายการ/วัน**")
    # ----------------------------------------------