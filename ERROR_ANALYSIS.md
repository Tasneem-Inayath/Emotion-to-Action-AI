# Error Analysis

The model was evaluated on multiple challenging scenarios to understand its limitations.

---

## Case 1 — Short Text
- Input: "ok"
- Issue: insufficient information
- Reason: TF-IDF cannot extract meaning
- Fix: uncertainty flag (implemented)

---

## Case 2 — Ambiguous Input
- Input: "I don’t know how I feel"
- Issue: unclear emotion
- Reason: no strong features
- Fix: introduce ambiguity handling

---

## Case 3 — Conflicting Signals
- Input: "I feel fine"
- Metadata: stress=9, energy=2
- Issue: contradiction
- Reason: text vs metadata conflict
- Fix: weight metadata more

---

## Case 4 — Focused Misclassified
- Input: "I feel ready to work"
- Predicted: calm
- Issue: semantic gap
- Reason: TF-IDF lacks understanding
- Fix: keyword boosting / embeddings

---

## Case 5 — Noisy Labels
- Input: "I feel great"
- Label: neutral
- Issue: incorrect training label
- Fix: dataset cleaning

---

## Case 6 — Very Short Input
- Input: "fine"
- Issue: unreliable prediction
- Fix: uncertainty flag

---

## Case 7 — Rare Words
- Input: "melancholic and drained"
- Issue: unseen vocabulary
- Fix: better embeddings

---

## Case 8 — Overgeneralization
- Input: "I'm okay"
- Issue: always predicted as calm
- Fix: diversify training data

---

## Case 9 — Missing Context
- Input: "tired"
- Issue: lacks supporting features
- Fix: use defaults / ask user

---

## Case 10 — Mixed Emotions
- Input: "calm but anxious"
- Issue: multiple emotions
- Fix: multi-label classification

---

## Insights

- Model performs well on clear signals
- Struggles with ambiguity and short text
- Uncertainty mechanism helps prevent overconfidence

---

## Conclusion

The system demonstrates realistic behavior under noisy and imperfect conditions, with uncertainty awareness improving reliability.