import google.generativeai as genai
from PIL import Image

# 🔑 ใส่ API KEY ของนายตรงนี้ให้เรียบร้อย
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

def load_ai_model():
    """โหลดสมอง Gemini รุ่นใหม่ล่าสุดที่เก่งเรื่องการมองเห็น"""
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # 🌟 เปลี่ยนชื่อตรงนี้เป็นรุ่นที่มีในเครื่องนาย (gemini-2.5-flash)
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def analyze_image(img, model):
    """ส่งรูปให้ AI ดู จัดหมวดหมู่ และดึงรายละเอียดเชิงลึก"""
    if model is None:
        return "ERROR_MODEL_NOT_LOADED", "ไม่สามารถโหลด AI ได้"
    
    try:
        # Prompt ใหม่ที่รีดพลัง AI ขั้นสุด
        prompt = """
        Analyze this image and provide exactly 2 things separated by a pipe symbol (|).
        
        Part 1 - Exact Category: Choose ONLY ONE from this list:
        Animal, Person, Food, Document, Anime, Landscape, Others.
        
        Part 2 - Details: 
        - If it's a 'Document', extract the main text, topic, or total price.
        - If it's a 'Wireframe/UI', describe the layout structure.
        - Otherwise, give a short 1-sentence description in Thai language.
        
        Format example:
        Document|ใบเสร็จค่าอาหาร ยอดรวม 250 บาท
        Animal|แมวลายสลิดกำลังจ้องมองกล้อง
        """
        
        # ส่งรูปและคำสั่งไปให้ Gemini
        response = model.generate_content([prompt, img])
        raw_text = response.text.strip().replace("\n", "")
        
        print(f"🤖 [DEBUG] AI ตอบมาว่า: '{raw_text}'")
        
        # แยกข้อความด้วยเครื่องหมาย |
        if "|" in raw_text:
            category, details = raw_text.split("|", 1)
            category = category.strip().capitalize()
            details = details.strip()
        else:
            category = "Others"
            details = raw_text
        
        # เช็คความถูกต้องของหมวดหมู่
        valid_categories = ["Animal", "Person", "Food", "Document", "Anime", "Landscape", "Others"]
        if category not in valid_categories:
            category = "Others"
            
        return category, details
        
    except Exception as e:
        print(f"❌ [API ERROR] พังเพราะ: {e}")
        return "ERROR", f"เกิดข้อผิดพลาด: {str(e)[:50]}"