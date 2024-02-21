from mtcnn import MTCNN
import cv2

def detect_faces(frame):
    detector = MTCNN()
    
    result = detector.detect_faces(frame)

    faces = []
    if result:
        for face_info in result:
            bounding_box = face_info['box']
            x, y, w, h = [max(0, coord) for coord in bounding_box]
            face = frame[y:y+h, x:x+w]
            faces.append(face)

    return faces

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

        # Display the original frame
        cv2.imshow('Original Frame', frame)

        # Display each detected face
        for idx, face in enumerate(detected_faces):
            cv2.imshow(f'Detected Face {idx}', face)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
