import os
import shutil
import pandas as pd
from PIL import Image
import zipfile
from io import BytesIO

def ensure_user_folders(username):
    """สร้างโครงสร้างโฟลเดอร์พื้นฐานให้ User ทันทีที่ Login"""
    base_path = f"Users/{username}/AI_Sorted"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    for sub in ['Images', 'Documents', 'Others']:
        path = f"Users/{username}/{sub}"
        if not os.path.exists(path):
            os.makedirs(path)
    return base_path

def get_stats(username):
    """สถิติเฉพาะของแต่ละ User"""
    data = {"Category": [], "Count": []}
    base_path = f"Users/{username}"
    
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):
                count = sum([len(files) for r, d, files in os.walk(folder_path)])
                data["Category"].append(folder)
                data["Count"].append(count)
                
    return pd.DataFrame(data)

def save_uploaded_file(uploaded_file, target_subfolder, final_name):
    """บันทึกไฟล์ลงในพื้นที่ User"""
    if not os.path.exists(target_subfolder):
        os.makedirs(target_subfolder)
    
    save_path = os.path.join(target_subfolder, final_name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def sweep_folder(folder_path, ai_model, username):
    """กวาดไฟล์จากภายนอก เข้าสู่พื้นที่ของ User"""
    import ai_engine  
    report = []
    if not os.path.exists(folder_path):
        return None, "ไม่พบที่อยู่โฟลเดอร์นี้ครับ"

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue
            
        ext = os.path.splitext(filename)[1].lower()
        user_base = f"Users/{username}"

        if ext in [".jpg", ".jpeg", ".png"]:
            img = Image.open(file_path)
            detected = ai_engine.analyze_image(img, ai_model)
            category = detected[0] if detected else "unclassified_images"
            dest_dir = f"{user_base}/AI_Sorted/{category}"
        elif ext in [".pdf", ".docx", ".txt"]:
            dest_dir = f"{user_base}/Documents"
        else:
            continue 

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        shutil.move(file_path, os.path.join(dest_dir, filename))
        report.append(f"✅ ย้าย {filename} -> {dest_dir}")
        
    return report, "กวาดเรียบร้อย!"

# --- ฟังก์ชันใหม่สำหรับ Day 2 ---

def log_action(username, filename, category, status="Success"):
    """บันทึกประวัติแยกตาม User พร้อมฟอร์แมตเวลาให้สวยงาม"""
    log_file = f"Users/{username}/activity_log.csv"
    
    # บันทึกเวลาแบบอ่านง่าย (YYYY-MM-DD HH:MM:SS)
    current_time = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_data = pd.DataFrame([[current_time, filename, category, status]], 
                            columns=["Time", "Filename", "Category", "Status"])
    
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
        
    if not os.path.exists(log_file):
        new_data.to_csv(log_file, index=False, encoding='utf-8-sig') # ใช้ utf-8-sig เพื่อให้อ่านไทยใน Excel ได้
    else:
        new_data.to_csv(log_file, mode='a', header=False, index=False, encoding='utf-8-sig')

def get_activity_log(username):
    """ดึงข้อมูลประวัติย้อนหลังมาแสดงผล เรียงจากใหม่ไปเก่า"""
    log_file = f"Users/{username}/activity_log.csv"
    if os.path.exists(log_file):
        try:
            df = pd.read_csv(log_file)
            # เรียงลำดับจากเวลาล่าสุดขึ้นก่อน
            return df.sort_values(by="Time", ascending=False)
        except:
            return pd.DataFrame(columns=["Time", "Filename", "Category", "Status"])
    return pd.DataFrame(columns=["Time", "Filename", "Category", "Status"])

def delete_file(file_path):
    """ลบไฟล์ออกจากระบบ"""
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False

def create_zip_of_folder(folder_path):
    """บีบอัดไฟล์ในโฟลเดอร์เป็น ZIP สำหรับดาวน์โหลด"""
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                z.write(os.path.join(root, file), file)
    return buf.getvalue()