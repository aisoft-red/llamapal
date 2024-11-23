import cv2
import pyttsx3

def overlay_text(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return frame

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
