import streamlit_authenticator as stauth

# เวอร์ชันล่าสุดใช้การเรียกฟังก์ชัน hash ตรงๆ จากคลาส Hasher ได้เลย
hashed_passwords = stauth.Hasher.hash('1234')

print(hashed_passwords)