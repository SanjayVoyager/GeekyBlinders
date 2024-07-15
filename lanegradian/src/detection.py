import cv2
import numpy as np

class Detection:
    def __init__(self, model, video_path):
        self.model = model
        self.video_path = video_path

    def detect_cut_in(self, frame):
        input_frame = cv2.resize(frame, (128, 128))
        input_frame = np.expand_dims(input_frame, axis=0)
        prediction = self.model.predict(input_frame)
        return prediction

    def real_time_detection(self):
        cap = cv2.VideoCapture(self.video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            prediction = self.detect_cut_in(frame)
            # Implement logic to alert based on prediction
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
