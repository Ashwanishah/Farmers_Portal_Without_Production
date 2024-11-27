
# Farmer Portal

Welcome to the Farmer Portal, a comprehensive platform designed to assist farmers with essential recommendations to enhance crop yield and health. The portal includes three key features: Crop Recommendation, Fertilizer Recommendation, and Disease Prediction using a Convolutional Neural Network (CNN) model.

---

## Features

### 1. Crop Recommendation
The Crop Recommendation system suggests the best crop to grow based on specific soil and environmental parameters such as:
- **Nutrient Levels**: Nitrogen (N), Phosphorus (P), Potassium (K)
- **Environmental Conditions**: Temperature, Humidity, pH, and Rainfall

By analyzing these factors, the system provides a tailored crop recommendation to help farmers maximize productivity.

### 2. Fertilizer Recommendation
The Fertilizer Recommendation system assists farmers in identifying the right type and amount of fertilizer to use, based on the crop type and soil conditions. The system evaluates soil nutrient levels and recommends the ideal fertilizer to maintain balanced soil health and improve crop growth.

### 3. Disease Prediction
The Disease Prediction feature uses a Convolutional Neural Network (CNN) to identify diseases in plants from leaf images. Farmers can upload an image of a plant's leaf, and the system will predict the likelihood of common plant diseases. This allows for early intervention and effective treatment, ensuring healthier crops.

---

## Technology Stack

- **Backend**: Python, Flask
- **Machine Learning Libraries**: scikit-learn, TensorFlow/Keras for CNN
- **Data Processing**: Pandas, NumPy
- **Web Interface**: HTML, CSS

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/farmer-portal.git
   cd farmer-portal
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## Usage

1. **Crop Recommendation**: Enter the required soil and environmental parameters to receive a crop suggestion.
2. **Fertilizer Recommendation**: Select the crop and provide soil nutrient levels to get a fertilizer recommendation.
3. **Disease Prediction**: Upload a photo of a leaf, and the system will predict any potential diseases.

---

## Models

- **Crop Recommendation Model**: A machine learning model trained to predict the most suitable crop based on soil and weather conditions.
- **Fertilizer Recommendation Model**: A rule-based or trained model to suggest the ideal fertilizer mix.
- **Disease Prediction Model**: A CNN model trained on a dataset of plant leaf images to detect diseases.

---

## Project Structure

```plaintext
farmer-portal/
├── app.py                                   # Main application file
├── requirements.txt                         # Required Python libraries
├── Templates/                               # HTML templates
├── forms/                                   # Forms
├── Crop_Recommendation_system/              # Pre-trained models
├── Fertilizer Prediction/                   # Pre-trained models
├── Plant Prediction/                        # Pre-trained models
├── uploads/                                 # Uploded Photographs of plant
└── README.md                                # Project documentation
```

---

## Contributing

We welcome contributions! If you'd like to contribute to this project, please fork the repository and submit a pull request.

---

## Acknowledgements

Special thanks to the open-source community and the datasets used to train the models.

---
