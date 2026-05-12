# 🚗💰 Car Price Predictor

> *Know what your car is worth — instantly.*

A sleek, end-to-end **Machine Learning web app** that predicts the resale value of used cars in seconds. Just enter your car's details and let the model do the math.

---

## ✨ What It Does

Feed it a car. Get a price. That simple.

Under the hood, a **Random Forest Regressor** trained on real-world used car data analyzes features like manufacturing year, kilometers driven, fuel type, and more — then returns an accurate price estimate via a lightning-fast API.

---

## 🏗️ Architecture

```
 [ Streamlit UI ]  ──── HTTP POST ────▶  [ FastAPI Backend ]  ────▶  [ ML Model ]
   (Frontend)           /predict           (REST API)               (Random Forest)
```

| Layer | Technology |
|---|---|
| 🎨 Frontend | Streamlit |
| ⚡ Backend | FastAPI + Uvicorn |
| 🧠 ML Model | scikit-learn (Random Forest Regressor) |
| 🔢 Data | pandas |
| 🐍 Language | Python 3.12 |

---

## 🚀 Run It Locally

**1. Clone & Install**
```bash
git clone https://github.com/vikashg450/Car-Price-Prediction-.git
cd Car-Price-Prediction-
pip install -r requirements.txt
```

**2. Start the Backend**
```bash
uvicorn main:app --reload
# API live at → http://localhost:8000
```

**3. Launch the Frontend** *(new terminal)*
```bash
streamlit run streamlit_app.py
# UI live at → http://localhost:8501
```

---

## 🌐 Deployment

| Component | Platform | Config |
|---|---|---|
| ⚙️ Backend | [Render.com]([https://car-price-predict-385b.onrender.com]) | Uses included `Procfile` |
| 🎨 Frontend | [Streamlit Cloud]([https://car-price-predict-b2ujwb8yit9flmiflzpjgc.streamlit.app/]) | Set `API_URL` env variable |

> 💡 **Tip:** After deploying the backend to Render, copy its public URL and set it as `API_URL` in your Streamlit Cloud environment settings.

---

## 🔮 Input Features

| Feature | Description |
|---|---|
| 📅 Year | Manufacturing year of the car |
| 📍 Kilometers Driven | Total distance covered |
| ⛽ Fuel Type | Petrol / Diesel / CNG |
| 🧑‍💼 Seller Type | Dealer or Individual |
| ⚙️ Transmission | Manual or Automatic |
| 👤 Owner | Number of previous owners |

---

## 📁 Project Structure

```
car-price-api/
├── main.py              # FastAPI app & /predict endpoint
├── streamlit_app.py     # Streamlit frontend UI
├── model.pkl            # Trained Random Forest model
├── requirements.txt     # All dependencies
└── Procfile             # Render deployment config
```

---

## 👨‍💻 Author

**Vikash** — [@vikashg450](https://github.com/vikashg450)

---

<p align="center">Made with ❤️ and Python</p>
