import numpy as np
import pyautogui
import imutils
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # Acceder a las marcas de referencia por su posición
          

            # Matriz para almacenar "True" o "False" si el dedo está doblado
       
                # Obteniendo las marcas de referencia de las posición de las puntas y dibujando un círculo azul
      

                # Escribiendo una condición para verificar si el dedo está doblado, 
                # es decir, si el valor inicial de la punta del dedo es menor que 
                # la posición inicial del dedo, que es la marca de referencia interior.
                # Para el índice del dedo, si el dedo está doblado, cambiar el color a verde
             

             # Verificar si todos los dedos están doblados
    
                # Tomar una captura de pantalla y almacenarla en la memorioa,
                # luego convertir la imagen PIL/Pillow a un arreglo NumPy compatible con OpenCV.
                # Finalmente, escribir la imagen en el disco
            

                # Esta vez, toma una captura de pantalla directamente al disco
         

                # Entonces, podemos cargar nuestra captura de pantalla desde el disco en formato OpenCV
        





            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("Seguimiento de manos", img)
    cv2.waitKey(1)






