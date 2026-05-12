import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ai_engine
import file_utils
import shutil
from win10toast import ToastNotifier # เพิ่มตัวแจ้งเตือน

# สร้างตัวส่ง Notification
toaster = ToastNotifier()
WATCH_PATH = r"C:\Users\User\Downloads"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            ext = os.path.splitext(filename)[1].lower()
            
            # ข้ามไฟล์ชั่วคราว (เช่น .tmp, .crdownload) ที่ยังโหลดไม่เสร็จ
            if ext in [".tmp", ".crdownload"]:
                return

            time.sleep(2) # รอให้โหลดไฟล์เสร็จสมบูรณ์จริงๆ
            
            print(f"👀 ตรวจพบไฟล์ใหม่: {filename}")
            
            # ส่วนเช็คประเภทไฟล์เหมือนเดิม
            if ext in [".jpg", ".jpeg", ".png"]:
                from PIL import Image
                model = ai_engine.load_ai_model()
                img = Image.open(event.src_path)
                detected = ai_engine.analyze_image(img, model)
                category = detected[0] if detected else "Others"
                target_folder = f"AI_Sorted/{category}"
            elif ext in [".pdf", ".docx", ".txt"]:
                category = "Documents"
                target_folder = category
            else:
                return

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            try:
                shutil.move(event.src_path, os.path.join(target_folder, filename))
                
                # --- ส่วนที่ทำให้มันเด้งเตือนบนหน้าจอคอม ---
                toaster.show_toast(
                    "AI File Master 3000",
                    f"กวาดเรียบร้อย! ย้าย {filename} ไปที่ {target_folder}",
                    duration=5,
                    threaded=True
                )
                print(f"✅ ย้ายสำเร็จ!")
            except Exception as e:
                print(f"❌ ย้ายไม่ได้: {e}")

if __name__ == "__main__":
    # โค้ดส่วนรัน Observer เหมือนเดิม...
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)
    observer.start()
    print(f"🚀 ยามเริ่มเฝ้าโฟลเดอร์: {WATCH_PATH}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()