import streamlit as st
import os
import file_utils
import ai_engine

if not st.session_state.get('authentication_status'):
    st.warning("🔒 กรุณาเข้าสู่ระบบที่หน้าหลัก (app.py) ก่อนใช้งานครับ")
    st.stop()

username = st.session_state['username']
model = ai_engine.load_ai_model()

st.markdown("<h2 style='color: #4A90E2;'>🧹 ระบบกวาดล้างโฟลเดอร์อัตโนมัติ</h2>", unsafe_allow_html=True)
st.write(f"ระบุ Path เพื่อให้ AI กวาดไฟล์เข้าสู่พื้นที่ของ **{username}**")

folder_to_sweep = st.text_input("ระบุที่อยู่โฟลเดอร์ (เช่น C:/Downloads):", key=f"sweep_path_{username}")

if st.button("🔥 เริ่มการสแกนและย้ายไฟล์อัตโนมัติ"):
    if folder_to_sweep:
        
        # --- 🛡️ เพิ่มระบบป้องกัน: Blacklist โฟลเดอร์อันตราย ---
        forbidden_paths = ["C:/", "C:\\", "C:/Windows", "C:/Program Files", "/"]
        
        # เช็คว่า Path ที่พิมพ์มา ตรงกับโฟลเดอร์ต้องห้ามไหม
        is_forbidden = any(folder_to_sweep.startswith(bad_path) for bad_path in forbidden_paths)
        
        if is_forbidden:
            st.error("🚨 ไม่อนุญาตให้ดึงไฟล์จากโฟลเดอร์ระบบ (System Folders) เพื่อความปลอดภัยครับ!")
        # -----------------------------------------------------
        
        elif os.path.exists(folder_to_sweep):
            with st.spinner("AI กำลังจัดระเบียบไฟล์เข้าสู่พื้นที่ของคุณ..."):
                results, msg = file_utils.sweep_folder(
                    folder_path=folder_to_sweep, 
                    ai_model=model, 
                    username=username
                )
                
                if results:
                    st.toast(f"กวาดไฟล์เสร็จแล้ว {len(results)} รายการ!", icon='🧹')
                    st.success(msg)
                    with st.expander("รายละเอียดการทำงานอย่างละเอียด"):
                        for line in results: 
                            st.write(line)
                    st.balloons()
                    
                    file_utils.log_action(username, "Batch Sweep", folder_to_sweep, "Success")
                else:
                    st.warning("ไม่พบไฟล์รูปภาพหรือเอกสารที่ AI จัดการได้ในโฟลเดอร์นี้")
        else:
            st.error("❌ ไม่พบโฟลเดอร์ตาม Path ที่ระบุ กรุณาตรวจสอบความถูกต้องอีกครั้ง")
    else:
        st.error("⚠️ กรุณากรอก Path โฟลเดอร์ที่ต้องการให้ AI ช่วยกวาดครับ")