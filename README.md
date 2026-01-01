# Restaurant Demand Forecasting System

> AI-powered forecasting tool helping a local bagel shop reduce waste by predicting daily demand


## Problem Statement and Purpose
I have always wanted to do a project that combines my passions in engineering and restaurants. When I worked at El Bagel, it upset me how many bagels were thrown out on some days.
I realized I could make an ML model that incorporates various data points to predict as accurately as possible the number of bagels the shop will sell on a given day, and therefore how many they will need to make. The manager told me that he currently calculates it manually week-by-week, and this could be helpful.

## Tech Stack

### Languages & Core Libraries
- **Python 3.9+**
- **SQL** - Data extraction and manipulation
- **Pandas, NumPy** - Data processing and feature engineering
- **scikit-learn** - Machine learning models (Random Forest, XGBoost being evaluated)

### Infrastructure & Tools
- **SQLite** - Local database for transaction history
- **FastAPI** - Backend API for model serving
- **Streamlit** - Frontend dashboard for business user
- **External APIs** - Weather data, local event calendars


## Features

### Current Implementation
-  Multi-feature prediction pipeline (day-of-week, seasonality, weather, events)
-  Historical data integration (2 years of POS transactions)
-  User-friendly Streamlit interface for non-technical users
-  FastAPI backend for model serving
-  Newsvendor optimization for safety stock calculations

### In Development
- 🔄 Real-time model retraining pipeline
- 🔄 A/B testing framework for model comparison
- 🔄 Mobile-responsive dashboard
- 🔄 Automated data quality checks

---

## 📊 Key Results

### Target Business Impact
- Waste Reduction: >= 50% decrease in daily overproduction
- Cost Savings; ~$200/day in labor costs
- Service Level: Maintaining 95% target (Newsvendor problem - selling out more costly than overproduction)

### Technical Performance
- Model: Random Forest regression (currently evaluating XGBoost)
- Features: 15+ engineered features (temporal, weather, event-based)
- Data: 2 years of daily transaction records
- Optimization: Newsvendor critical ratio applied to inventory decisions

### Product Success Metrics
- User Adoption: Designed for zero-training adoption by shop owner
- Actionability: 2-day forecast horizon matches inventory ordering cycle
- Reliability: Built-in data quality checks and model monitoring


*Built with the goal of turning AI technology into practical solutions for small businesses.*# restaurant-demand-forecastAI-powered demand forecasting system to reduce food and labor waste for local deli
