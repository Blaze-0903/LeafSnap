# 🌿 LeafSnap+ - Medicinal Plant Identifier

[![Streamlit App](https://img.shields.io/badge/Launch%20App-LeafSnap+-brightgreen?logo=streamlit)](https://leafsnap-7g8ydx3wapsv2jvyedaafg.streamlit.app/)

LeafSnap+ is a deep learning-based web application that identifies **medicinal plants** from images of their leaves and suggests **natural remedies** or uses based on the identified plant. Powered by **TensorFlow/Keras** and built using **Streamlit**, it provides a simple interface for both plant recognition and healthcare insights.

---

## 🔗 Live Demo

➡️ **[Click here to use the app](https://leafsnap-7g8ydx3wapsv2jvyedaafg.streamlit.app/)**

---

## 📸 Features

- 🌱 Upload or capture an image of a leaf
- 🧠 Classify it using a trained CNN model (`.h5` file)
- ✅ Display the predicted plant name with confidence score
- 💊 Show suggested remedies/uses for the plant
- 💻 Built with Python, TensorFlow, Keras, and Streamlit

---

## 🖼 Sample Screenshot

![LeafSnap+ Screenshot](https://user-images.githubusercontent.com/your-screenshot-link.png) <!-- Optional -->

---

## 🚀 Technology Stack

- **Frontend/UI:** Streamlit
- **Backend:** TensorFlow + Keras (CNN model)
- **Language:** Python
- **Model Format:** `.h5` file (pre-trained using plant leaf dataset)

---

## 🧪 How It Works

1. User uploads or captures a leaf image.
2. Image is preprocessed (resized, normalized).
3. A TensorFlow model predicts the plant class.
4. The app displays:
   - 🌿 Predicted Plant Name
   - 📊 Confidence Score
   - 💊 Medicinal Remedy/Use

---

## 🛠 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Blaze-0903/LeafSnap.git
cd LeafSnap
```

### 2. Create & Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Model File

Since GitHub limits uploads >25MB, the model file is stored on Google Drive.

📥 **Download the model (`LeafSnap_model.h5`) from this link:**

[https://drive.google.com/file/d/1IM9BZYmPNM1-FH0rQAmZDKLrHdv7o8Qx/view](https://drive.google.com/file/d/1IM9BZYmPNM1-FH0rQAmZDKLrHdv7o8Qx/view)

Then place the downloaded file in the project root directory.

```
LeafSnap/
├── app.py
├── LeafSnap_model.h5   <-- put it here
├── requirements.txt
├── ...
```

### 5. Run the App Locally

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
LeafSnap/
│
├── app.py                  # Main Streamlit app
├── LeafSnap_model.h5       # Trained model file
├── requirements.txt        # Project dependencies
├── README.md               # Project readme
└── ...
```

---

## 🧠 Why TensorFlow & Keras?

- **Keras** provides a high-level API that makes model building and loading very simple.
- **TensorFlow** is the backend engine that runs the model efficiently, even for real-time inference.

---

## 👤 Author

**Blaze-0903**  
📬 [GitHub Profile](https://github.com/Blaze-0903)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💬 Feedback & Contributions

Feel free to fork this repo, improve it, and submit pull requests. Issues and suggestions are always welcome!
