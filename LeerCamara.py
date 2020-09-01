import cv2

cap = cv2.VideoCapture("prueba1.mp4")
cap.open("prueba1.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('prueba',frame)
    cv2.waitkey(0)