from data_preparation import DataPreparation
from model_definition import ModelDefinition
from training import Training
from detection import Detection

def main():
    # Data Preparation
    data_preparation = DataPreparation('data/path_to_dataset')
    images, labels = data_preparation.load_dataset()
    X_train, X_test, y_train, y_test = data_preparation.preprocess_data(images, labels)

    # Model Definition
    model_definition = ModelDefinition()
    model = model_definition.create_model()

    # Training
    training = Training(model, X_train, y_train, X_test, y_test)
    training.train_model(epochs=10)
    training.evaluate_model()

    # Real-Time Detection
    detection = Detection(model, 'path_to_video')
    detection.real_time_detection()

if __name__ == "__main__":
    main()
