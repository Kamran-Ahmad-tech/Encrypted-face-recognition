import cv2
import os
import numpy as np
from cryptography.fernet import Fernet

DATA = "faces"
KEY = "key.key"
os.makedirs(DATA, exist_ok=True)

# --- Encryption Key ---
def load_key():
    if not os.path.exists(KEY):
        k = Fernet.generate_key()
        open(KEY, 'wb').write(k)
    return open(KEY, 'rb').read()

cipher = Fernet(load_key())

def encrypt(b):
    return cipher.encrypt(b)

def decrypt(b):
    return cipher.decrypt(b)

# --- Camera Capture ---
def capture():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("❌ Camera not accessible")
        return None

    print("Press S to capture face, ESC to exit")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("❌ Failed to read from camera")
            break

        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            cam.release()
            cv2.destroyAllWindows()
            return frame
        elif key == 27:
            cam.release()
            cv2.destroyAllWindows()
            exit()

# --- Face Detection + Normalization ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("❌ No face detected")
        return None

    x, y, w, h = faces[0]
    face = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
    face = cv2.equalizeHist(face)

    return face

# --- Register Face ---
def register():
    name = input("Enter Name: ")

    img = capture()
    if img is None:
        return

    face = get_face(img)
    if face is None:
        return

    enc_data = encrypt(face.tobytes())
    open(f"{DATA}/{name}.dat", "wb").write(enc_data)

    print("✅ Face registered & encrypted successfully!")

# --- Recognize Face ---
def recognize():
    img = capture()
    if img is None:
        return

    face = get_face(img)
    if face is None:
        return

    for f in os.listdir(DATA):
        name = f.split(".")[0]
        enc = open(f"{DATA}/{f}", "rb").read()

        try:
            known = np.frombuffer(decrypt(enc), dtype=np.uint8).reshape(100, 100)
        except:
            continue

        diff = np.mean((face - known) ** 2)

        if diff < 50:  # threshold
            print("✅ MATCH FOUND:", name)
            return

    print("❌ MATCH NOT FOUND")

# --- Menu ---
while True:
    print("\n--- MENU ---")
    print("1 - Register Face")
    print("2 - Recognize Face")
    print("Q - Quit")

    ch = input("Choice: ")

    if ch == "1":
        register()
    elif ch == "2":
        recognize()
    elif ch.lower() == "q":
        break
    else:
        print("Invalid choice!")
