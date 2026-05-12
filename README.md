# 🤖 AI File Master 3000

The Great Organizer - ระบบจัดการและวิเคราะห์ไฟล์อัจฉริยะ ขับเคลื่อนด้วยขุมพลัง AI (Gemini 2.5 Flash) ช่วยเปลี่ยนการจัดการไฟล์ที่น่าเบื่อให้เป็นเรื่องง่ายและอัตโนมัติ

## ✨ ฟีเจอร์หลัก (Key Features)

* **🧠 AI File Categorization:** อัปโหลดรูปภาพ แล้วให้ AI วิเคราะห์รายละเอียด ดึงข้อความ และจัดหมวดหมู่ไฟล์ให้อัตโนมัติ (Animal, Person, Document, UI/Wireframe ฯลฯ)
* **🪄 Sketch to Code (ฟีเจอร์พิเศษ):** อัปโหลดภาพร่างหน้าจอ (Wireframe) แล้วให้ AI แปลงเป็นโค้ด HTML/CSS พร้อมหน้าต่าง Preview แบบเรียลไทม์
* **💬 AI Chat Assistant:** แชทบอทอัจฉริยะที่เชื่อมต่อกับฐานข้อมูลไฟล์ของคุณ สามารถถาม-ตอบ สรุปสถิติ และค้นหาข้อมูลไฟล์ได้เหมือนคุยกับผู้ช่วยส่วนตัว
* **📊 Data Dashboard:** หน้าแสดงผลสถิติการใช้งานกราฟิกสวยงาม (Plotly) พร้อมระบบส่งออกข้อมูล (Export to CSV)
* **🧹 Batch Sweep:** ระบบกวาดไฟล์อัตโนมัติ สแกนโฟลเดอร์ที่กำหนดและจัดระเบียบไฟล์เข้าที่อย่างรวดเร็ว
* **🔒 Secure Login System:** ระบบรักษาความปลอดภัยด้วยรหัสผ่าน แยกพื้นที่การจัดเก็บไฟล์ของผู้ใช้แต่ละคนอย่างชัดเจน

## 🛠️ เครื่องมือที่ใช้ (Tech Stack)

* **Frontend & UI:** Streamlit
* **AI Engine:** Google Gemini API (gemini-2.5-flash)
* **Data Visualization:** Pandas, Plotly Express
* **Image Processing:** Pillow (PIL)
* **Authentication:** Streamlit-Authenticator

## 🚀 วิธีการติดตั้งและรันโปรแกรม

1. โคลนโปรเจคนี้ลงมาที่เครื่องของคุณ
2. ติดตั้งไลบรารีที่จำเป็นด้วยคำสั่ง:
   ```bash
   pip install -r requirements.txt