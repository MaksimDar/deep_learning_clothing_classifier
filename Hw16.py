import keras
import streamlit as st
from PIL import Image, ImageOps
import io
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import tensorflow as tf


### Виведіть графіки функції втрат і точності для моделі
def show_graph(history):
    accuracy_values = history['accuracy']
    val_accuracy_values = history['val_accuracy']

    loss_values = history['loss']
    val_loss_values = history['val_loss']
    
    epochs = range(1,len(accuracy_values) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(epochs, accuracy_values, 'bo', label='Training accuracy')
    ax1.plot(epochs, val_accuracy_values, 'b', label='Validation accuracy')
    ax1.set_title('Training and validation accuracy')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    
    ax2.plot(epochs, loss_values, 'bo', label='Training loss')
    ax2.plot(epochs, val_loss_values, 'b', label='Validation loss')
    ax2.set_title('Training and validation loss')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Loss')
    ax2.legend()

    plt.tight_layout()

    return fig


### 
list_categories = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']


model_cnn = keras.models.load_model("best_model_cnn.keras")
model_vgg16 = keras.models.load_model("best_model_vgg16.keras")


st.title('Модель класифікації для визначення типу одягу')

uploaded_file = st.file_uploader("Виберіть зображення...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='вхідне зображення')

    # Перетворення завантаженого зображення у відтінки сірого відповідно
    gray_image = ImageOps.grayscale(image)

    # Зміна розміру зображення до базової роздільної здатності 28x28
    resized_image = gray_image.resize((28,28))

    # Нормалізація значень пікселів до діапазону [0, 1]
    img_array = np.array(resized_image).astype('float32') / 255.0

    # Зміна форми масиву для додавання розмірності батчу та каналів
    image_input = img_array.reshape(-1, 28, 28, 1)

    model_type = st.radio('Виберіть модель для класифікації вашого зображення', ['CNN', 'VGG16'])

    if model_type == 'CNN':
        # Прогноз CNN
        predictions = model_cnn.predict(image_input)
    elif model_type == 'VGG16':
        # Прогноз VGG16
        image_input_vgg16 = tf.image.resize(tf.image.grayscale_to_rgb(tf.constant(image_input)), (48, 48))
        predictions = model_vgg16.predict(image_input_vgg16)

    st.write('Таблиця результатів')
    # st.write(predictions)

    # Таблиця ймовірностей для категорії «одяг»
    prob_df = pd.DataFrame({
        'Клас': list_categories,
        'Ймовірність (%)': (predictions[0] * 100).round(2)
    }).sort_values('Ймовірність (%)', ascending=False)

    st.write(prob_df)
    result = np.argmax(predictions,axis=1)
    result = result.astype('int')[0]
    result_category = list_categories[result]
    pred_number = predictions[0][result]
    final_number = float(pred_number*100)
    precision = round(final_number,2)
    st.write(f'Згідно з таблицею результатів, на фотографії зображено {result_category} з точністю {precision}%.')

    ### Завантаження результатів моделей точності та втрат 
    if model_type == 'CNN':
        with open('history_cnn.json','r') as f:
            history_data = json.load(f)
    elif model_type == 'VGG16':
        with open('history_vgg16.json','r') as f:
            history_data = json.load(f)

    ### Демонстрації точності та втрат        
    st.write(f'Графіки функції втрат і точності моделі {model_type}')
    fig = show_graph(history_data)
    st.pyplot(fig)