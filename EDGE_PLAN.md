# 📱 Edge Deployment Plan

## 🎯 Goal
Deploy the system on lightweight environments such as mobile or edge devices.

---

## ⚙️ Deployment Approach

- Convert trained models to portable formats (ONNX / joblib)
- Run inference locally without cloud dependency
- Integrate with mobile or embedded systems

---

## 🧠 Model Design for Edge

- XGBoost chosen for:
  - fast inference
  - small size
  - efficient memory usage

- TF-IDF:
  - lightweight compared to deep models

---

## ⚡ Performance

- Expected latency: < 100 ms
- Suitable for real-time interaction
- Minimal computational overhead

---

## 🔧 Optimizations

- Reduce TF-IDF features if needed
- Use model quantization
- Preload models in memory
- Avoid redundant preprocessing

---

## 📦 System Components

- Model (.pkl files)
- TF-IDF vectorizer
- Encoders

All run locally without external APIs.

---

## ⚠️ Trade-offs

| Factor | Decision |
|------|--------|
| Accuracy | Moderate |
| Speed | High |
| Model Size | Small |
| Interpretability | High |

---

## 🧠 Robustness

The system handles:
- Short inputs (via uncertainty)
- Missing values (via defaults)
- Conflicting signals (via decision rules)

---

## 🚀 Future Improvements

- Replace TF-IDF with lightweight embeddings
- Improve handling of unseen categories
- Add on-device learning capabilities

---

## ✅ Conclusion

The system is suitable for real-world edge deployment due to its lightweight architecture, fast inference, and robustness to noisy inputs.