import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split

class DataPreparation:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def load_dataset(self):
        images = []
        labels = []
        for img_file in os.listdir(self.dataset_path):
            img_path = os.path.join(self.dataset_path, img_file)
            image = cv2.imread(img_path)
            images.append(image)
            label = self.extract_label_from_filename(img_file)
            labels.append(label)
        return np.array(images), np.array(labels)

    def extract_label_from_filename(self, filename):
        # Implement label extraction logic
        pass

    def preprocess_data(self, images, labels):
        X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
