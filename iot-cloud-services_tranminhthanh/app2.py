import firebase_admin
from firebase_admin import credentials, db

# 1. Kết nối Firebase
cred = credentials.Certificate("tran-minh-thanh-firebase-adminsdk-fbsvc-8f069934b7.json")  # File key tải từ Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tran-minh-thanh-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Lấy toàn bộ dữ liệu
ref = db.reference("environment_data")
data = ref.get()

if data:
    print("📊 Dữ liệu môi trường:")
    temps = []
    for key, entry in data.items():
        print(entry)
        temps.append(entry["Temperature"])
    
    avg_temp = sum(temps) / len(temps)
    print(f"🌡 Nhiệt độ trung bình: {avg_temp:.2f}°C")
else:
    print("Không có dữ liệu.")
