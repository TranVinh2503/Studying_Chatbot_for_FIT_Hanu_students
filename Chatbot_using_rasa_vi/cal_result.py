def evaluate_online(model, data_stream):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    
    for new_instance in data_stream:
        prediction = model.predict(new_instance.features)
        if prediction == new_instance.true_label:
            if prediction == Positive:
                TP += 1
            else:
                TN += 1
        else:
            if prediction == Positive:
                FP += 1
            else:
                FN += 1
                
        accuracy = (TP + TN) / (TP + TN + FP + FN)
        precision = TP / (TP + FP) if TP + FP != 0 else 0
        recall = TP / (TP + FN) if TP + FN != 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall != 0 else 0
        
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-Score:", f1_score)