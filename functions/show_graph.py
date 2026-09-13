### Виведіть графіки функції втрат і точності для моделі
import matplotlib.pyplot as plt
import streamlit as st

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
    st.pyplot(fig)