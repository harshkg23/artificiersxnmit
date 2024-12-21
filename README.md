# Lung Cancer Detector

Lung Cancer Detector is a web application that leverages machine learning to predict whether an X-ray image indicates the presence of lung cancer. The backend uses a pre-trained AI model to classify the images, while the frontend is built using HTML and CSS. Firebase is used as the database for storing user data and other information.

## **Table of Contents**
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## **Features**
- **AI Model**: Uses a pre-trained machine learning model for detecting lung cancer from X-ray images.
- **Frontend**: Built using HTML and CSS to provide a simple and responsive user interface.
- **Firebase**: Integrated Firebase for storing and managing user data.
- **Prediction**: The model predicts whether the image contains signs of lung cancer (Malignant or Benign).
- **Image Upload**: Upload an X-ray image for prediction.
- **Result Display**: Displays the result of the prediction (Malignant/Benign) along with the uploaded image.

## **Tech Stack**
- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Machine Learning**: TensorFlow/Keras (for the model)
- **Database**: Firebase
- **Model**: Pre-trained deep learning model (model.h5)
- **File Handling**: PIL (for image processing)


## **Installation**

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/harshkg23/artificiersxnmit.git
   cd artificiersxnmit
   ```
2. **Activate the virtual environment:**
   - On Windows:
  ```bash
  venv\Scripts\activate
  ```
   - On macOS/Linux:
  ```
  source venv/bin/activate
  ```
3. **Install the required Python packages**:
   ```bash
   pip install -r backend/requirements.txt
   ```

## **Usage**

1. Open the frontend at: [http://localhost:5000](http://localhost:5000).
2. Upload an X-ray image using the provided file upload form.
3. The AI model will process the image and predict whether it is Malignant or Benign.
4. The result will be displayed on the results page along with the uploaded image.
5. The result is also stored in the Firebase database for reference.

## **Contact**
- **Author**: Harsh Kumar Gupta  
- **Email**: harshkumargupta2023@gmail.com  
- **GitHub**: [https://github.com/harshkg23](https://github.com/harshkg23)






