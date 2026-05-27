import streamlit as st
import os
import file_utils
from styles import apply_custom_css
apply_custom_css()

if not st.session_state.get('authentication_status'):
    st.warning("🔒 กรุณาเข้าสู่ระบบที่หน้าหลัก (app.py) ก่อนใช้งานครับ")
    st.stop()

username = st.session_state['username']

st.markdown("<h2 style='color: #4A90E2;'>🖼️ คลังไฟล์ส่วนตัวของคุณ</h2>", unsafe_allow_html=True)
user_ai_path = f"Users/{username}/AI_Sorted"

if os.path.exists(user_ai_path):
    categories = os.listdir(user_ai_path)
    if categories:
        head_col1, head_col2 = st.columns([3, 1])
        
        with head_col1:
            selected_cat = st.selectbox("เลือกหมวดหมู่ที่ต้องการจัดการ:", categories)
        
        cat_path = os.path.join(user_ai_path, selected_cat)
        
        with head_col2:
            st.write("---") 
            zip_data = file_utils.create_zip_of_folder(cat_path)
            st.download_button(
                label="📦 โหลดหมวดนี้ (ZIP)",
                data=zip_data,
                file_name=f"{selected_cat}_{username}.zip",
                mime="application/zip",
                help="ดาวน์โหลดไฟล์ทั้งหมดในหมวดนี้เป็นไฟล์เดียว"
            )

        st.divider()
        files = [f for f in os.listdir(cat_path) if os.path.isfile(os.path.join(cat_path, f))]
        
        if files:
            for file_name in files:
                full_path = os.path.join(cat_path, file_name)
                with st.container():
                    col_img, col_info, col_btn = st.columns([1, 3, 1])
                    
                    with col_img:
                        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                            st.image(full_path, use_container_width=True)
                        else:
                            st.write("📄 **FILE**") 
                    
                    with col_info:
                        st.write(f"**ชื่อไฟล์:** `{file_name}`")
                        file_size = os.path.getsize(full_path) / 1024
                        st.caption(f"ขนาดไฟล์: {file_size:.2f} KB | ที่อยู่: {selected_cat}")
                    
                    with col_btn:
                        st.write("") 
                        if st.button("🗑️ ลบไฟล์", key=f"del_{file_name}"):
                            if file_utils.delete_file(full_path):
                                file_utils.log_action(username, file_name, selected_cat, "Deleted")
                                st.toast(f"ลบไฟล์ {file_name} ออกจากระบบแล้ว", icon="🗑️")
                                st.rerun()
                    st.write("---")
        else:
            st.info("หมวดหมู่ว่างเปล่า")
    else:
        st.info("ยังไม่มีหมวดหมู่ที่ถูกสร้างขึ้น")
else:
    st.info("คลังไฟล์ยังว่างเปล่า เริ่มอัปโหลดไฟล์แรกของคุณได้เลย!")