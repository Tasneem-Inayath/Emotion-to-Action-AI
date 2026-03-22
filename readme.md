# Emotion → Action AI System

## Overview
This project builds an intelligent system that goes beyond prediction.  
It understands user emotions, reasons under uncertainty, and suggests meaningful actions.

The system consists of:
- Emotional understanding (state + intensity)
- Decision engine (what to do + when)
- Uncertainty modeling
- Supportive conversational response
- API + UI for interaction

---

## Setup Instructions

### 1. Clone project
git clone <your-repo-link>
cd emotion_to_action_ai

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate


### 3. Install dependencies

pip install requirements.txt


---

## How to Run

### Step 1 — Run API

uvicorn api:app --reload


### Step 2 — Run Streamlit UI
streamlit run app.py


---

## Approach

The system is designed as a 3-layer architecture:

### 1. Understanding Layer (ML)
- Predicts emotional_state
- Predicts intensity (1–5)

### 2. Decision Layer
- Uses rules based on:
  - predicted state
  - intensity
  - stress
  - energy
  - time of day
- Outputs:
  - what_to_do
  - when_to_do

### 3. Guidance Layer
- Generates human-like supportive message

---

## Feature Engineering

### Text Features
- TF-IDF vectorization
- n-grams (1 to 3)
- stopword removal

### Metadata Features
- sleep_hours
- stress_level
- energy_level
- time_of_day
- previous_day_mood
- ambience_type
- reflection_quality

### Final Input
- Combined text + metadata using sparse matrix stacking

---

## Model Choice

### Emotional State
- Model: XGBoost Classifier
- Reason: Handles tabular + sparse data effectively

### Intensity
- Model: XGBoost Classifier
- Reason: Discrete ordinal values (1–5)

---

## Uncertainty Modeling

- Confidence = weighted probability from models
- Uncertain flag triggered when:
  - confidence < 0.6
  - very short input text

---

## Key Design Decisions

- Hybrid approach (ML + rule-based)
- Lightweight models for edge deployment
- Avoided heavy LLMs (as per constraints)
- Focused on real-world noisy input handling

---

## Output

The system produces:
- predicted_state
- predicted_intensity
- confidence
- uncertain_flag
- what_to_do
- when_to_do
- supportive message

---

## Goal

AI should not just understand humans —  
it should guide them toward better mental states.

## Demo
- FastAPI backend
- Streamlit chatbot UI
- Emotion → Action decision system

## Sample Image
<image>

# By Author :
Tasneem Firdhosh,MCA

# Contact:
tasneemfirdhosh2001@gmail.com
