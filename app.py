import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import file_utils
from styles import apply_custom_css
apply_custom_css()

# --- 1. ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="AI File Master 3000", page_icon="🤖", layout="wide")

# --- 2. ระบบ Login ---
with open('config.yaml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    auto_hash=False 
)

auth_data = authenticator.login('main', fields={'Form name': 'เข้าสู่ระบบ AI File Master'})
authentication_status = st.session_state.get('authentication_status')

# ---------------------------------------------------------
# CASE 1: ล็อกอินสำเร็จ
# ---------------------------------------------------------
if authentication_status:
    username = st.session_state.get('username')
    name = st.session_state.get('name')

    file_utils.ensure_user_folders(username)

    # --- UI: Banner ต้อนรับ ---
    st.markdown(f"<h1 style='text-align: center; color: #4A90E2; margin-top: -30px;'>🤖 AI File Master 3000</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center; color: #6c757d;'>ยินดีต้อนรับกลับมาครับคุณ <b>{name}</b> 👋</h4>", unsafe_allow_html=True)
    st.divider()
    
    # --- UI: แนะนำฟีเจอร์หลัก (ใช้ Columns จัด Layout สไตล์ SaaS) ---
    st.write("### 🚀 เลือกใช้งานฟีเจอร์จากเมนูด้านซ้าย")
    st.write("") # เว้นบรรทัด
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.info("#### 📥 อัปโหลด & สแกน\n\nให้สมอง AI ช่วยวิเคราะห์รูปภาพและแยกหมวดหมู่ไฟล์ของคุณโดยอัตโนมัติ ไม่ต้องทำเองให้เหนื่อย")
    with c2:
        st.success("#### 🖼️ คลังไฟล์ส่วนตัว\n\nจัดการ ดาวน์โหลดเป็น ZIP และลบไฟล์ของคุณได้อย่างง่ายดายผ่านระบบ Gallery ส่วนตัว")
    with c3:
        st.warning("#### 📊 สถิติข้อมูล\n\nดูรายงานสรุปการทำงานรายวัน ส่งออกข้อมูลเป็น Excel และเช็คกราฟสัดส่วนไฟล์ในระบบ")
    with c4:
        st.error("#### 💬 AI Chatbot\n\nระบบผู้ช่วยอัจฉริยะที่รู้จักไฟล์ของคุณ พิมพ์สั่งงานหรือสอบถามข้อมูลได้เหมือนคุยกับมนุษย์")

    st.write("<br><br>", unsafe_allow_html=True)
    
    # ภาพประกอบด้านล่าง
    st.image("https://images.unsplash.com/photo-1618477247222-ac60f36f0e42?q=80&w=1200&auto=format&fit=crop", 
             use_container_width=True, 
             caption="The Great Organizer - Powered by AI")

    # --- SIDEBAR ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3588/3588632.png", width=100)
        st.title("User Profile")
        st.success(f"Username: **{username}**")
        authenticator.logout('ออกจากระบบ', 'sidebar')
        st.divider()
        st.write("👨‍💻 **Developer:** นายวิชานนท์ วิชชุกรศักดิ์")

# ---------------------------------------------------------
# CASE 2: ตรวจสอบสถานะการ Login
# ---------------------------------------------------------
elif authentication_status is False:
    st.error('Username หรือ Password ไม่ถูกต้อง')
elif authentication_status is None:
    st.warning('กรุณาเข้าสู่ระบบเพื่อเริ่มใช้งานระบบ AI จัดการไฟล์')