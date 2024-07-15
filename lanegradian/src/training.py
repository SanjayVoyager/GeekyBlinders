class Training:
    def __init__(self, model, X_train, y_train, X_test, y_test):
        self.model = model
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test

    def train_model(self, epochs=10):
        history = self.model.fit(self.X_train, self.y_train, epochs=epochs, validation_data=(self.X_test, self.y_test))
        return history

    def evaluate_model(self):
        test_loss, test_acc = self.model.evaluate(self.X_test, self.y_test)
        print(f'Test accuracy: {test_acc}')
        return test_loss, test_acc
