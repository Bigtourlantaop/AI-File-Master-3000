import streamlit as st
import os
from PIL import Image
import ai_engine
import file_utils

# 🔒 ระบบป้องกัน: เช็คว่า Login หรือยัง
if not st.session_state.get('authentication_status'):
    st.warning("🔒 กรุณาเข้าสู่ระบบที่หน้าหลัก (app.py) ก่อนใช้งานครับ")
    st.stop() # หยุดการทำงานของหน้านี้ทันที

username = st.session_state['username']
model = ai_engine.load_ai_model()

st.markdown("<h2 style='color: #4A90E2;'>📤 อัปโหลด & สแกนด้วย AI</h2>", unsafe_allow_html=True)
st.divider()

left_col, right_col = st.columns([1, 1])
with left_col:
    st.subheader("📥 อัปโหลดไฟล์ใหม่")
    uploaded_file = st.file_uploader("เลือกไฟล์จากเครื่องคุณ...", type=None, key="uploader")

if uploaded_file is not None:
    # --- 🛡️ เพิ่มระบบป้องกัน: เช็คขนาดไฟล์ (จำกัดที่ 5MB) ---
    MAX_FILE_SIZE = 5 * 1024 * 1024 # 5 MB แปลงเป็น Bytes
    
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("❌ ไฟล์มีขนาดใหญ่เกินไปครับ! (กรุณาอัปโหลดไฟล์ขนาดไม่เกิน 5MB)")
    else:
        # ถ้าไฟล์ขนาดผ่านเกณฑ์ ค่อยให้ระบบทำงานต่อ
        with right_col:
            st.subheader("🔍 วิเคราะห์โดย AI")
            suggested_name = uploaded_file.name
            user_base = f"Users/{username}"
            target_subfolder = f"{user_base}/Others"

            if uploaded_file.type.startswith("image"):
                img = Image.open(uploaded_file)
                st.image(img, width=300)
                
                with st.spinner("🧠 AI กำลังวิเคราะห์ข้อมูลเชิงลึก..."):
                    category, details = ai_engine.analyze_image(img, model)
                
                if category and not category.startswith("ERROR"):
                    st.success(f"📁 หมวดหมู่: **{category}**")
                    st.info(f"📝 รายละเอียด: {details}") 
                    
                    suggested_name = f"{category}_{uploaded_file.name}"
                    target_subfolder = f"{user_base}/AI_Sorted/{category}"
                else:
                    st.warning("🤖 AI ไม่แน่ใจว่าเป็นรูปอะไร หรือเกิดข้อผิดพลาด")
                    st.error(details) 
                    target_subfolder = f"{user_base}/Images"

            final_name = st.text_input("📝 ตั้งชื่อไฟล์ใหม่:", value=suggested_name)

            if st.button("✅ ยืนยันการบันทึกไฟล์"):
                file_utils.save_uploaded_file(uploaded_file, target_subfolder, final_name)
                file_utils.log_action(username, final_name, target_subfolder, "Success")
                st.toast(f"บันทึกไฟล์ {final_name} สำเร็จ!", icon="✅")
                st.balloons()
                st.success(f"จัดเก็บลงใน {target_subfolder} เรียบร้อย!")