import google.generativeai as genai

# 🔑 สำคัญมาก: เอา API Key ของนายที่ขึ้นต้นด้วย "AIza..." มาใส่ตรงนี้!
GEMINI_API_KEY = "AIzaSyB2hEjFfwgsWSC0RbLWdJv-q_6uffbcBO8"

try:
    genai.configure(api_key=GEMINI_API_KEY)
    print("🔍 กำลังเชื่อมต่อกับ Google และสแกนหาโมเดลที่ใช้งานได้...\n")
    
    # ดึงรายชื่อโมเดลทั้งหมดออกมา
    found_vision_model = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ พบโมเดล: {m.name}")
            if "vision" in m.name or "flash" in m.name:
                found_vision_model = True
                
    print("\n------------------------------------------------")
    if found_vision_model:
        print("🎉 เยี่ยมมาก! คุณมีโมเดลที่ดูรูปภาพได้ ให้ก๊อปปี้ชื่อด้านบน (เช่น models/gemini-1.5-flash-001) ไปใส่ใน ai_engine.py ได้เลย")
    else:
        print("⚠️ ไม่พบโมเดลสำหรับดูรูป (API Key นี้อาจจะมีสิทธิ์จำกัด)")

except Exception as e:
    print(f"❌ พัง! เชื่อมต่อไม่ได้: {e}")