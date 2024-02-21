import cv2
import numpy as np
from PIL import Image
from google.deepdream import deepdream  # Import the deepdream module from the cloned repository

def enhance_faces(faces):
    enhanced_faces = []

    for face in faces:
        # Convert OpenCV BGR image to RGB (required by deepdream)
        face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Convert to PIL Image
        face_pil = Image.fromarray(face_rgb)

        # Apply DeepDream enhancement
        enhanced_face = deepdream.deepdream(face_pil)

        # Convert back to OpenCV BGR image
        enhanced_face_bgr = cv2.cvtColor(np.array(enhanced_face), cv2.COLOR_RGB2BGR)

        enhanced_faces.append(enhanced_face_bgr)

    return enhanced_faces

if __name__ == "__main__":
    # Example usage for testing
    video_path = 'path/to/your/video.mp4'
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Example: Using the detect_faces function
        detected_faces = detect_faces(frame)

        # Example: Using the enhance_faces function
        enhanced_faces = enhance_faces(detected_faces)

        # Display the original frame
        cv2.imshow('Original Frame', frame)

        # Display each enhanced face
        for idx, enhanced_face in enumerate(enhanced_faces):
            cv2.imshow(f'Enhanced Face {idx}', enhanced_face)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
