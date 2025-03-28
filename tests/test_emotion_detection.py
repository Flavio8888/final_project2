import unittest
import json
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'joy')

    def test_anger(self):
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'anger')

    def test_disgust(self):
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'disgust')

    def test_sadness(self):
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'sadness')

    def test_fear(self):
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        result_dict = json.loads(result)
        self.assertEqual(result_dict['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
