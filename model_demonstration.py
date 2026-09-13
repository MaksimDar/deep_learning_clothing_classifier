import keras
import streamlit as st
from PIL import Image, ImageOps
import io
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import tensorflow as tf

from functions import show_graph
from translations import TRANSLATIONS


list_categories_en = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
list_categories_uk = ['Футболка/топ','Штани','Пуловер','Сукня','Пальто','Сандалі', 'Сорочка','Кросівки','Сумка','Черевики']
model_cnn = keras.models.load_model("best_model_cnn.keras")
model_vgg16 = keras.models.load_model("best_model_vgg16.keras")
language = st.session_state.language
lang_status = 'en' if language == 'English' else 'uk'
list_categories = list_categories_en if lang_status == 'en' else list_categories_uk
t = TRANSLATIONS[lang_status]

st.title(t['title'])
uploaded_file = st.file_uploader(t['image_upload'], type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption=t['input_image'])

    # Перетворення завантаженого зображення у відтінки сірого відповідно
    gray_image = ImageOps.grayscale(image)

    # Зміна розміру зображення до базової роздільної здатності 28x28
    resized_image = gray_image.resize((28,28))

    # Нормалізація значень пікселів до діапазону [0, 1]
    img_array = np.array(resized_image).astype('float32') / 255.0

    # Зміна форми масиву для додавання розмірності батчу та каналів
    image_input = img_array.reshape(-1, 28, 28, 1)
    model_type = st.radio(t['model_select'], ['CNN', 'VGG16'])

    if model_type == 'CNN':
        # Прогноз CNN
        predictions = model_cnn.predict(image_input)
    elif model_type == 'VGG16':
        # Прогноз VGG16
        image_input_vgg16 = tf.image.resize(tf.image.grayscale_to_rgb(tf.constant(image_input)), (48, 48))
        predictions = model_vgg16.predict(image_input_vgg16)

    st.write(t['results_table'])
     # st.write(predictions)

    # Таблиця ймовірностей для категорії «одяг»
    prob_df = pd.DataFrame({
        t['class']: list_categories,
        t['probability']: (predictions[0] * 100).round(2)
    }).sort_values(t['probability'], ascending=False)

    st.write(prob_df)
    result = np.argmax(predictions,axis=1)
    result = result.astype('int')[0]
    result_category = list_categories[result]
    pred_number = predictions[0][result]
    final_number = float(pred_number*100)
    precision = round(final_number,2)
    st.write(f"{t['table_show_result']} {result_category} {t['precision']} {precision}%.")

    ### Завантаження результатів моделей точності та втрат 
    if model_type == 'CNN':
        with open('history_cnn.json','r') as f:
            history_data = json.load(f)
    elif model_type == 'VGG16':
        with open('history_vgg16.json','r') as f:
            history_data = json.load(f)

    ### Демонстрації точності та втрат        
    st.write(f"{t['graph']} {model_type}")
    show_graph(history_data)
    st.markdown(f"## {t['conclusion']}:")
    st.write(t['conclusion_text'])
