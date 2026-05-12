# Car Price Prediction 🚗💰

This is a complete Machine Learning application that predicts the selling price of used cars based on their features (Year, Kilometers Driven, Fuel Type, Seller Type, etc.).

## Project Architecture
This project is split into two components:
1. **Backend (FastAPI)**: Serves the Machine Learning model via a REST API.
2. **Frontend (Streamlit)**: Provides a user-friendly UI to input car details and display the predicted price.

## Tech Stack
* **Python 3.12**
* **Machine Learning**: `scikit-learn` (Random Forest Regressor), `pandas`
* **API Engine**: `FastAPI`, `uvicorn`, `pydantic`
* **UI**: `Streamlit`

## How to run locally

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Backend API:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Run the Frontend UI:** (In a separate terminal)
   ```bash
   streamlit run streamlit_app.py
   ```

## Deployment
* **Backend**: Can be deployed to Render.com using the included `Procfile`.
* **Frontend**: Can be deployed to Streamlit Community Cloud. Ensure you set the `API_URL` environment variable to point to your deployed backend.
