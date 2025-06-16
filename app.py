import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io
import base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



# ------------------- Must be First ------------------- #
st.set_page_config(page_title="LeafSnap+ - Medicinal Plant Identifier", layout="centered")

# ------------------- Load Model ------------------- #
@st.cache_resource
def load_trained_model():
    model = load_model("LeafSnap_model.h5")
    return model

model = load_trained_model()

# ------------------- Class Labels ------------------- #
CLASS_LABELS = ['Aloe Vera', 'Amla', 'Amruthaballi', 'Arali', 'Astma Weed', 'Badipala', 'Balloon Vine', 'Bamboo', 'Beans', 'Betel', 'Bhrami', 'Bringaraja', 'Caricature', 'Castor', 'Catharanthus', 'Chakte', 'Chilly', 'Citron Lime (herelikai)', 'Coffee', 'Common Rue(naagdalli)', 'Coriender', 'Curry', 'Doddpathre', 'Drumstick', 'Ekka', 'Eucalyptus', 'Ganigale', 'Ganike', 'Gasagase', 'Ginger', 'Globe Amarnath', 'Guava', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jackfruit', 'Jasmine', 'Kambajala', 'Kasambruga', 'Kohlrabi', 'Lantana', 'Lemon', 'Lemongrass', 'Malabar Nut', 'Malabar Spinach', 'Mango', 'Marigold', 'Mint', 'Neem', 'Nelavembu', 'Nerale', 'Nooni', 'Onion', 'Padri', 'Palak(Spinach)', 'Papaya', 'Parijatha', 'Pea', 'Pepper', 'Pomoegranate', 'Pumpkin', 'Raddish', 'Rose', 'Sampige', 'Sapota', 'Seethaashoka', 'Seethapala', 'Spinach1', 'Tamarind', 'Taro', 'Tecoma', 'Thumbe', 'Tomato', 'Tulsi', 'Turmeric', 'ashoka', 'camphor', 'kamakasturi', 'kepala']
IMAGE_SIZE = (224, 224)

# ------------------- Style and Theme ------------------- #
bg_image_base64 = get_base64_image("static/background.png")  # Use your actual path

st.markdown(f"""
    <style>
        html, body, .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #f0fdf4;
        }}
        .title {{
            text-align: center;
            color: #d4f5e6;
            font-size: 3rem;
            font-weight: 900;
            margin-top: 10px;
        }}
        .subtitle {{
            text-align: center;
            color: #c6f6d5;
            font-size: 1.2rem;
            margin-bottom: 30px;
        }}
        .info-box {{
            background-color: #e6ffedcc;
            padding: 1rem;
            border-radius: 12px;
            border-left: 5px solid #38a169;
            margin-bottom: 20px;
            color: #1a202c;
            font-weight: 600;
        }}
        .stButton > button {{
            background-color: #38a169;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }}
        .stRadio > div {{
            background: linear-gradient(145deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
            backdrop-filter: blur(4px);
            padding: 10px;
            border-radius: 10px;
            border: 2px solid white;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
        .middle-box-wrapper {{
            max-width: 1400px;
            margin: auto;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(6px);
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid #ffffff55;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            margin-bottom: 2rem;
        }}
        .middle-box {{
            padding: 1.5rem;
        }}
        h2, .stFileUploader label, .stCameraInput label {{
            color: #e6fffa !important;
            font-weight: bold !important;
        }}
        .stRadio label span {{
            color: #f0fff4 !important;
            font-weight: bold !important;
        }}
        .stRadio label {{
            color: #f0fff4 !important;
            font-weight: bold !important;
        }}
        .footer {{
            text-align: center;
            font-size: 0.9rem;
            color: #e2e8f0;
            margin-top: 50px;
            padding: 10px;
        }}
    </style>
""", unsafe_allow_html=True)


# ------------------- Titles ------------------- #
st.markdown('<div class="title">🍃 LeafSnap+</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Medicinal Plant Identifier & Natural Remedies Guide</div>', unsafe_allow_html=True)

# ------------------- Helper Functions ------------------- #
def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.resize(IMAGE_SIZE)
    image_array = np.array(image) / 255.0
    if image_array.shape[-1] == 4:
        image_array = image_array[..., :3]
    return np.expand_dims(image_array, axis=0)

def predict(image: Image.Image) -> str:
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)[0]
    class_idx = np.argmax(predictions)
    confidence = predictions[class_idx]
    return CLASS_LABELS[class_idx], confidence

def display_remedy(plant_name):
    remedies = {
        "Aloe Vera": "Soothes burns and aids digestion.",
        "Amla": "Rich in Vitamin C, boosts immunity.",
        "Amruthaballi": "Helps in controlling fever and detoxification.",
        "Arali": "Used in traditional medicine for skin issues.",
        "Astma weed": "Traditional remedy for asthma relief.",
        "Badipala": "Known to help with swelling and pain.",
        "Balloon Vine": "Treats joint pain and stiffness.",
        "Bamboo": "Used in traditional bone healing.",
        "Beans": "Nutritious and supports heart health.",
        "Betel": "Aids digestion and freshens breath.",
        "Bhrami": "Boosts brain function and memory.",
        "Bringaraja": "Promotes hair growth and liver health.",
        "Caricature": "Used for respiratory disorders.",
        "Castor": "Relieves constipation and hair health.",
        "Catharanthus": "Contains anti-cancer compounds.",
        "Chakte": "Used for controlling sugar levels.",
        "Chilly": "Boosts metabolism and has antioxidants.",
        "Citron Lime (herelikai)": "Aids digestion and immune support.",
        "Coffee": "Antioxidant-rich, boosts alertness.",
        "Common Rue(naagdalli)": "Treats insect bites and muscle pain.",
        "Coriender": "Improves digestion and skin.",
        "Curry": "Improves vision and digestive health.",
        "Doddpathre": "Used for cough and cold.",
        "Drumstick": "Rich in iron and vitamins.",
        "Ekka": "Used in Ayurveda for ulcers.",
        "Eucalyptus": "Clears nasal congestion.",
        "Ganigale": "Traditional pain reliever.",
        "Ganike": "Detoxifying and supports liver health.",
        "Gasagase": "Improves sleep and reduces anxiety.",
        "Ginger": "Eases nausea and inflammation.",
        "Globe Amarnath": "Used to cool the body.",
        "Guava": "Boosts immunity and improves skin.",
        "Henna": "Natural hair dye and coolant.",
        "Hibiscus": "Controls blood pressure and cholesterol.",
        "Honge": "Used as antiseptic and mosquito repellent.",
        "Insulin": "Lowers blood sugar levels.",
        "Jackfruit": "Rich in fiber and vitamins.",
        "Jasmine": "Reduces stress and improves sleep.",
        "Kambajala": "Traditional remedy for inflammation.",
        "Kasambruga": "Used in skin and hair care.",
        "Kohlrabi": "Rich in vitamin C and fiber.",
        "Lantana": "Used externally for skin diseases.",
        "Lemon": "Boosts immunity and detoxifies.",
        "Lemongrass": "Reduces anxiety and cholesterol.",
        "Malabar Nut": "Used for respiratory conditions.",
        "Malabar Spinach": "Rich in iron and calcium.",
        "Mango": "Improves digestion and skin.",
        "Marigold": "Antiseptic and wound healing.",
        "Mint": "Aids digestion and relieves nausea.",
        "Neem": "Powerful antibacterial and antifungal.",
        "Nelavembu": "Used for fever and immunity.",
        "Nerale": "Supports diabetic health.",
        "Nooni": "Immunity booster and detox aid.",
        "Onion": "Supports heart health.",
        "Padri": "Used in skin treatments.",
        "Palak(Spinach)": "Iron-rich and boosts energy.",
        "Papaya": "Aids digestion and skin health.",
        "Parijatha": "Treats cough and cold.",
        "Pea": "High in protein and fiber.",
        "Pepper": "Enhances digestion and absorption.",
        "Pomoegranate": "Rich in antioxidants.",
        "Pumpkin": "Boosts immunity and eye health.",
        "Raddish": "Improves liver function.",
        "Rose": "Used in skincare and mood lifting.",
        "Sampige": "Used for aroma and skincare.",
        "Sapota": "Boosts energy and digestion.",
        "Seethaashoka": "Women’s health tonic.",
        "Seethapala": "Rich in vitamins.",
        "Spinach1": "Nutrient-dense leafy green.",
        "Tamarind": "Improves digestion.",
        "Taro": "Good for gut and immunity.",
        "Tecoma": "Used for diabetes.",
        "Thumbe": "Traditional flower used in rituals.",
        "Tomato": "Rich in lycopene.",
        "Tulsi": "Immunity and respiratory aid.",
        "Turmeric": "Anti-inflammatory powerhouse.",
        "ashoka": "Supports reproductive health.",
        "camphor": "Used for cough and cold.",
        "kamakasturi": "Aromatic and medicinal uses.",
        "kepala": "Traditional herb with many uses."
    }
    return remedies.get(plant_name, "Remedy information not available.")

# ------------------- Input Section ------------------- #
st.markdown("## 📷 Upload a Leaf Image or Use Your Camera")

option = st.radio("Select input method:", ["Upload Image", "Use Camera"])

image = None
if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose a leaf image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
elif option == "Use Camera":
    captured_image = st.camera_input("Capture a leaf image")
    if captured_image is not None:
        image = Image.open(captured_image)

# ------------------- Prediction and Result ------------------- #
if image:
    st.image(image, caption="🌿 Your Input Image", use_column_width=True)
    plant_name, confidence = predict(image)

    st.success(f"✅ Identified: **{plant_name}** with **{confidence*100:.2f}%** confidence")
    st.markdown("---")

    st.markdown("### 🌱 Medicinal Uses")
    st.markdown(f"<div class='info-box'>{display_remedy(plant_name)}</div>", unsafe_allow_html=True)

    st.markdown("### 🧪 Confidence Level")
    st.progress(int(confidence * 100))

    st.markdown("---")
    st.info("🔔 This AI model is for educational purposes. Please consult a healthcare provider before using herbal remedies.")

# ------------------- Footer ------------------- #
st.markdown("""
    <hr style="margin-top: 40px;">
    <div class="footer">
        © 2025 LeafSnap+ | All Rights Reserved
    </div>
""", unsafe_allow_html=True)
