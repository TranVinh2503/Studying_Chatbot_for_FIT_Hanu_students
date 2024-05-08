from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class EvaluateModel(Action):
    def name(self) -> Text:
        return "action_evaluate_model"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        conversations = tracker.events
        for event in conversations:
            if event.get("event") == "user":
                user_utterance = event.get("text")
                # Assuming you have a function to label the user utterance
                true_label = label_user_utterance(user_utterance)
                bot_response = get_bot_response(user_utterance)
                # Assuming you have a function to predict the intent using your model
                predicted_label = predict_intent(user_utterance)
                if true_label == predicted_label:
                    if predicted_label == "positive":
                        TP += 1
                    else:
                        TN += 1
                else:
                    if predicted_label == "positive":
                        FP += 1
                    else:
                        FN += 1

        accuracy = (TP + TN) / (TP + TN + FP + FN)
        precision = TP / (TP + FP) if TP + FP != 0 else 0
        recall = TP / (TP + FN) if TP + FN != 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 0

        dispatcher.utter_message(text=f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-Score: {f1_score}")

        return []

def label_user_utterance(utterance: Text) -> Text:
    # Here you can implement your logic to label user utterances, it can be manual labeling or using some pre-trained model.
    # For simplicity, I'm returning a dummy label here.
    # Replace this with your actual labeling logic.
    return "positive" if "happy" in utterance.lower() else "negative"

def get_bot_response(utterance: Text) -> Text:
    # Assuming you have a function to generate bot responses based on user utterances.
    # Replace this with your actual bot response generation logic.
    return "I'm glad to hear that!" if "happy" in utterance.lower() else "I'm sorry to hear that!"

def predict_intent(utterance: Text) -> Text:
    # Assuming you have a function to predict the intent of user utterances using your model.
    # Replace this with your actual prediction logic.
    return "positive" if "happy" in utterance.lower() else "negative"


evaluate_model_action = EvaluateModel()


evaluate_model_action.run(dispatcher, tracker, domain)