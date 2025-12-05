# Encrypted Face Recognition System

A Python-based face recognition project that captures faces using a webcam, normalizes the image, encrypts the face data using **Fernet (AES-based)** encryption, and later decrypts it for secure face matching.

---

## 🚀 Features
- Capture face from live webcam  
- Face detection using OpenCV Haar Cascades  
- Normalize image (grayscale + resize + histogram equalization)  
- Encrypt face data using Fernet  
- Store encrypted faces locally  
- Decrypt & compare for verification  
- Simple menu-based interface  

---

## 📂 Project Structure
```
face-encrypt-recognize/
│
├── code/
│   └── face_recog.py        # main script
├── requirements.txt         # dependencies
├── .gitignore               # keeps secrets & face data private
└── README.md                # documentation
```

---

## 🛠 Installation

### 1. Clone Repository
```bash
git clone https://github.com/your-username/encrypted-face-recognition.git
cd encrypted-face-recognition
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the main script:

```bash
python code/face_recog.py
```

### Menu Options
| Option | Description |
|--------|-------------|
| `1` | Register a new face (captured + encrypted) |
| `2` | Recognize face from webcam |
| `Q` | Quit program |

---

## 🔐 Security Notes
- `key.key` **is not uploaded** — it's auto-generated locally.
- `faces/` folder (encrypted face data) is also kept private.
- Both are included inside `.gitignore`.
- For real-world usage, consider DNN face embeddings (OpenFace, FaceNet, etc.).

---

## 📜 License
You may use any license you prefer (MIT recommended).

