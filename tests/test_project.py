import unittest
from scripts.neural_network_model import model

class TestNeuralNetwork(unittest.TestCase):
    def test_model_not_none(self):
        self.assertIsNotNone(model, "Model should not be None")

    def test_model_accuracy(self):
        accuracy = model.evaluate(X_test, y_test)[1]
        self.assertGreater(accuracy, 0.8, "Accuracy should be greater than 80%")

if __name__ == "__main__":
    unittest.main()
