from rest_framework.generics import RetrieveAPIView, get_object_or_404, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from ...permissions import IsSafeToView
from ...serializers import MessageSerializer
import tensorflow as tf
import pickle as pkl
import numpy as np

class PredictNextWordView(UpdateAPIView):
    model = tf.keras.models.load_model("a1_api/api_views/AIStuff/nextword7.h5")
    tokenizer = pkl.load(open("a1_api/api_views/AIStuff/tokenizer7.pkl", "rb"))
    word_lookup = {v: k for k, v in tokenizer.word_index.items()}

    serializer_class = MessageSerializer
    def predict_next_word(self, text):
        """
            In this function we are using the tokenizer and models trained
            and we are creating the sequence of the text entered and then
            using our model to predict and return the predicted word.

        """
        text = text.lower().split(" ")
        try:
            sequence = PredictNextWordView.tokenizer.texts_to_sequences([text])[0]
            print(sequence)
            sequence = np.array(sequence)
            preds = PredictNextWordView.model.predict(sequence)
            pred = np.argmax(preds, axis=1)[-1]
            print(pred)
            return PredictNextWordView.word_lookup.get(pred, "")
        except ValueError:
            return ""

    def post(self, request, *args, **kwargs):
        data = request.data["data"].strip()
        prediction = self.predict_next_word(data)
        return Response({"message": prediction}, status=200)

