from fastapi import FastAPI
import joblib
import numpy as np
from scipy.sparse import csr_matrix, hstack
from decision import decide_action
from chatbot import chatbot_response


app = FastAPI()

# Load models
state_model = joblib.load("models/state_model.pkl")
intensity_model = joblib.load("models/intensity_model.pkl")
tfidf = joblib.load("models/tfidf.pkl")
encoders = joblib.load("models/encoders.pkl")
le_state = joblib.load("models/le_state.pkl")
le_intensity = joblib.load("models/le_intensity.pkl")


@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/predict")
def predict(data: dict):

    text = data["text"]
    sleep = data.get("sleep", 5)
    stress = data.get("stress", 5)
    energy = data.get("energy", 5)
    time_label = data["time"]

    # encode time
    time_label = time_label.lower()
    time_encoded = encoders["time_of_day"].transform([time_label])[0]

    # text → tfidf
    X_text = tfidf.transform([text.lower()])
    X_meta = np.array([[
        sleep,
        stress,
        energy,
        10,
        time_encoded,
        encoders["previous_day_mood"].transform([encoders["previous_day_mood"].classes_[0]])[0],
        encoders["face_emotion_hint"].transform([encoders["face_emotion_hint"].classes_[0]])[0],
        encoders["ambience_type"].transform([encoders["ambience_type"].classes_[0]])[0],
        encoders["reflection_quality"].transform([encoders["reflection_quality"].classes_[0]])[0]
    ]], dtype=np.float32)

    X_meta_sparse = csr_matrix(X_meta)
    X_input = hstack([X_text, X_meta_sparse])

    # predict state
    pred_state = state_model.predict(X_input)
    state = le_state.inverse_transform(pred_state)[0]

    pred_intensity = intensity_model.predict(X_input)[0]
    intensity = le_intensity.inverse_transform([pred_intensity])[0]
    # decision
    action, when = decide_action(state, intensity, stress, energy, time_encoded)

    # message
    message = chatbot_response(state, action, when)
    state_probs = state_model.predict_proba(X_input)
    state_conf = state_probs.max(axis=1)[0]

    int_probs = intensity_model.predict_proba(X_input)
    int_conf = int_probs.max(axis=1)[0]

    confidence = 0.7 * state_conf + 0.3 * int_conf
    
    text_len = len(text.split())
    uncertain_flag = int(confidence < 0.6 or text_len < 3)
    return {
        "state": str(state),
        "intensity": int(intensity),
        "action": str(action),
        "when": str(when),
        "message": str(message),
        "confidence": float(confidence),
        "uncertain_flag": int(uncertain_flag)
    }