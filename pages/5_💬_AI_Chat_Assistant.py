import streamlit as st
import file_utils
import ai_engine
import os
from styles import apply_custom_css
apply_custom_css()

# 🔒 เช็คระบบ Login
if not st.session_state.get('authentication_status'):
    st.warning("🔒 กรุณาเข้าสู่ระบบที่หน้าหลัก (app.py) ก่อนใช้งานครับ")
    st.stop()

username = st.session_state['username']
model = ai_engine.load_ai_model()

st.markdown("<h2 style='color: #4A90E2;'>💬 ผู้ช่วย AI ประจำคลังไฟล์</h2>", unsafe_allow_html=True)
st.write("พิมพ์ถามข้อมูลเกี่ยวกับไฟล์ของคุณ, ให้ช่วยค้นหา, หรือปรึกษาเรื่องการจัดระเบียบได้เลยครับ!")
st.divider()

# --- 1. เตรียมระบบความจำให้แชท (Chat History) ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"สวัสดีครับคุณ {username}! มีอะไรให้ผมช่วยหาหรือจัดการไฟล์ไหมครับ?"}]

# โชว์ข้อความแชทเก่าๆ บนหน้าจอ
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 2. กล่องพิมพ์ข้อความ (Chat Input) ---
if prompt := st.chat_input("พิมพ์ถาม เช่น: ตอนนี้ฉันมีไฟล์รูปแมวกี่ไฟล์?"):
    
    # เอาข้อความที่ User พิมพ์ไปโชว์บนจอ
    st.chat_message("user").markdown(prompt)
    # บันทึกลงความจำ
    st.session_state.messages.append({"role": "user", "content": prompt})

    # --- 3. ดึงข้อมูลไฟล์ไปให้ AI อ่านเบื้องหลัง ---
    df = file_utils.get_stats(username)
    log_df = file_utils.get_activity_log(username)
    
    # สร้างบริบท (Context) ให้ AI รู้จักไฟล์ของ User
    stats_data = df.to_dict('records') if not df.empty else 'ยังไม่มีไฟล์ในระบบ'
    recent_logs = log_df.tail(5).to_dict('records') if not log_df.empty else 'ไม่มีประวัติการทำงานล่าสุด'
    
    system_prompt = f"""
    คุณคือผู้ช่วย AI บริหารจัดการไฟล์อัจฉริยะ ช่วยเหลือผู้ใช้ชื่อ: {username}
    ข้อมูลไฟล์ในระบบตอนนี้: {stats_data}
    ประวัติการทำงานล่าสุด: {recent_logs}
    
    คำสั่ง: 
    1. ตอบคำถามของผู้ใช้อ้างอิงจากข้อมูลด้านบนให้เป็นธรรมชาติและสุภาพ
    2. ตอบเป็นภาษาไทย
    3. ถ้าผู้ใช้ถามเรื่องทั่วไปที่ไม่ได้เกี่ยวกับไฟล์ ก็ให้ตอบกลับในฐานะ AI ผู้ช่วยปกติ
    """

    # --- 4. ส่งไปให้ Gemini คิดและตอบกลับ ---
    with st.chat_message("assistant"):
        with st.spinner("🤖 AI กำลังประมวลผล..."):
            try:
                # เราใช้ generate_content ธรรมดา แต่เอา history แปะรวมเข้าไปใน Prompt 
                full_prompt = system_prompt + "\n\nคำถามของผู้ใช้: " + prompt
                response = model.generate_content(full_prompt)
                
                # โชว์คำตอบ
                st.markdown(response.text)
                # บันทึกคำตอบลงความจำ
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            
            except Exception as e:
                st.error(f"❌ ขัดข้องชั่วคราว: {e}")