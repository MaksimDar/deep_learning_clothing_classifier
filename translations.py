TRANSLATIONS = {
    'uk': {
        'title': 'Модель класифікації для визначення типу одягу',
        'image_upload': 'Завантажте зображення предмета одягу...',
        'input_image': 'вхідне зображення',
        'model_select': 'Виберіть модель для класифікації вашого зображення',
        'results_table': 'Таблиця результатів',
        'class': 'Клас',
        'probability': 'Ймовірність (%)',
        'table_show_result': 'Згідно з таблицею результатів, на фотографії зображено',
        'precision': 'з точністю',
        'graph': 'Графіки функції втрат і точності моделі',
        'conclusion': 'Висновок',
        'conclusion_text': 'VGG16 із донавчанням дала 92.41% — трохи краще за власну CNN (91.83%), але не значний стрибок. Спочатку, з повністю замороженою базою , точність трималась на рівні близько 85%, а після розморожування block4 і block5 з дуже малим learning rate вона піднялась до 92.41% — тобто саме донавчання дало приріст майже у 7 відсоткових пунктів.'

    },
    'en': {
        'title': 'Clothing Type Classification Model',
        'image_upload': 'Upload an image of a clothing item...',
        'input_image': 'input image',
        'model_select': 'Select a model to classify your image',
        'results_table': 'Results table',
        'class': 'Class',
        'probability': 'Probability (%)',
        'table_show_result': 'Based on the results table, in the image is illustrated ',
        'precision': 'with precision',
        'graph': 'Loss and accuracy graphs of the model',
        'conclusion': 'Conclusion',
        'conclusion_text': 'The VGG16 model with fine-tuning achieved 92.41%—slightly better than my own CNN (91.83%), but not a significant improvement. Initially, with the base model completely frozen, accuracy hovered around 85%, but after unfreezing blocks 4 and 5 with a very low learning rate, it rose to 92.41%—meaning that the fine-tuning alone resulted in a gain of nearly 7 percentage points.'

    }
}