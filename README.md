# 🏠 House Price Prediction App

A machine learning-powered web application that predicts house prices based on area, number of bedrooms, and property age. Built with Streamlit for an interactive user experience.

## 📋 Table of Contents
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Interactive Web Interface**: User-friendly Streamlit app with modern UI
- **Real-time Predictions**: Instant price estimates based on input parameters
- **Multiple Input Parameters**: 
  - Property area (sq. ft.)
  - Number of bedrooms
  - Age of property (years)
- **Responsive Design**: Clean and intuitive interface with custom styling
- **Visual Feedback**: Success animations and formatted price display

## 📊 Dataset

The model is trained on housing data with the following features:
- **Area**: Property size in square feet
- **Bedrooms**: Number of bedrooms in the house
- **Age**: Age of the property in years
- **Price**: Target variable (house price in currency units)

Sample data structure:
```csv
area,bedrooms,age,price
2600,3,20,550000
3000,4,15,565000
3200,3,18,610000
```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/area-price-prediction-use-condition-iitbhu.git
   cd area-price-prediction-use-condition-iitbhu
   ```

2. **Install required dependencies**:
   ```bash
   pip install streamlit pickle pandas scikit-learn
   ```

3. **Ensure model file exists**:
   Make sure `areapricebedage.pkl` is in the project directory

## 💻 Usage

### Running the Basic Version
```bash
streamlit run myfile2.py
```

### Running the Enhanced Version (Recommended)
```bash
streamlit run myfile2a.py
```

### Using the App
1. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)
2. Enter the property details:
   - **Area**: Property size in square feet (minimum 100 sq. ft.)
   - **Bedrooms**: Number of bedrooms (minimum 1)
   - **Age**: Property age in years (minimum 0)
3. Click "🔍 Predict Price" to get the estimated price
4. View the predicted price with visual confirmation

## 📁 Project Structure

```
area-price-prediction-use-condition-iitbhu/
├── README.md              # Project documentation
├── LICENSE               # License file
├── Multi.csv            # Training dataset
├── myfile2.py           # Basic Streamlit app
├── myfile2a.py          # Enhanced Streamlit app with styling
└── areapricebedage.pkl  # Trained ML model (pickle file)
```

## 🤖 Model Information

- **Model Type**: Machine Learning Regression Model
- **Input Features**: 3 numerical features (area, bedrooms, age)
- **Output**: Predicted house price
- **Format**: Serialized using Python's pickle module
- **File**: `areapricebedage.pkl`

### Model Usage
```python
import pickle
model = pickle.load(open("areapricebedage.pkl", "rb"))
prediction = model.predict([[area, bedrooms, age]])
```

## 🎨 App Versions

### Basic Version (`myfile2.py`)
- Simple interface
- Basic functionality
- Minimal styling

### Enhanced Version (`myfile2a.py`)
- Modern UI with custom CSS
- Responsive layout with columns
- Visual enhancements (icons, colors, animations)
- Better user experience
- Input validation and formatting

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web app framework
- **Pickle**: Model serialization
- **Scikit-learn**: Machine learning (implied)
- **Pandas**: Data manipulation (implied)
- **HTML/CSS**: Custom styling

## 📸 Screenshots

*Add screenshots of your application here*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add more input features (location, property type, etc.)
- [ ] Implement model retraining functionality
- [ ] Add data visualization charts
- [ ] Include model performance metrics
- [ ] Add export functionality for predictions
- [ ] Implement user authentication

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 👨‍💻 Author

Developed as part of IIT BHU practice project

---

**Note**: Make sure to have the trained model file (`areapricebedage.pkl`) in your project directory before running the application.