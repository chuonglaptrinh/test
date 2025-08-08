import speech_recognition as sr
import pyttsx3

# Khởi tạo bộ chuyển văn bản thành giọng nói
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Nhận giọng nói từ mic
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nói đi...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="vi-VN")  # nhận dạng tiếng Việt
        print("Bạn nói:", text)
        return text.lower()
    except:
        speak("Mình không nghe rõ, bạn nói lại nhé.")
        return ""

# Phân tích và tính toán
def process(text):
    if "cộng" in text:
        parts = text.replace("cộng", "").split()
        if len(parts) >= 2:
            try:
                a = float(parts[0])
                b = float(parts[1])
                result = a + b
                speak(f"Kết quả là {result}")
            except:
                speak("Không hiểu số bạn nói.")
    elif "trừ" in text:
        parts = text.replace("trừ", "").split()
        if len(parts) >= 2:
            try:
                a = float(parts[0])
                b = float(parts[1])
                result = a - b
                speak(f"Kết quả là {result}")
            except:
                speak("Không hiểu số bạn nói.")
    else:
        speak("Mình chỉ biết cộng và trừ thôi nha.")

# Vòng lặp chính
while True:
    text = listen()
    if "thoát" in text or "dừng" in text:
        speak("Tạm biệt nhé!")
        break
    process(text)


