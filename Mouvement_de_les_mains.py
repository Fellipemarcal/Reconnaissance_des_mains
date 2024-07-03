import cv2
import mediapipe as mp

# Inicialize a webcam
cap = cv2.VideoCapture(0)

# Crie um objeto MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

while True:
    # Leia um frame da webcam
    ret, frame = cap.read()
    
    # Converta o frame para RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Processa o frame com MediaPipe Hands
    results = hands.process(rgb)
    
    # Desenhe os resultados
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
    
    # Exiba o frame
    cv2.imshow('Hands', frame)
    
    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
cv2.destroyAllWindows()