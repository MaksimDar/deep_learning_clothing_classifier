# deep_learning_clothing_classifier

Clasificación de imágenes en el dataset Fashion-MNIST comparando una CNN propia (91.83% de precisión) con VGG16 mediante fine-tuning y transfer learning (92.41% de precisión), utilizando aumento de datos, EarlyStopping y programación de la tasa de aprendizaje. Incluye una aplicación en Streamlit para subir imágenes y ver predicciones en tiempo real con nivel de confianza y curvas de entrenamiento.

La aplicación admite interfaz en **ucraniano**, **inglés** y **español**, seleccionable desde la barra lateral.

## Configuración de los pesos del modelo

1. Descarga los pesos del modelo desde [este enlace de Google Drive](https://drive.google.com/file/d/1UXVYjxOxjt-ZB0cezdNeXF2-K3Bvxp5X/view?usp=sharing).
2. Coloca el archivo `vgg16_model.keras` en el directorio raíz del proyecto antes de ejecutar la aplicación de Streamlit.

## Ejecución local

```bash
conda activate clothing_classifier
streamlit run streamlit.py
```

La aplicación estará disponible en `http://localhost:8501` (o en el puerto que Streamlit indique en la terminal).

## Ejecución con Docker

Construir la imagen:

```bash
docker build . -t clothing-classifier
```

Ejecutar el contenedor:

```bash
docker run --name clothing-classification-app -p 8500:8501 -d clothing-classifier
```

La aplicación estará disponible en `http://localhost:8500`.

Ver los logs:

```bash
docker logs clothing-classification-app
```

Detener el contenedor:

```bash
docker stop clothing-classification-app
```

> **Nota:** los archivos `.keras` del modelo entrenado no están incluidos en este repositorio ni en el contexto de build de Docker debido a su tamaño. Asegúrate de que estén presentes en el directorio raíz del proyecto (ver *Configuración de los pesos del modelo* arriba) antes de construir la imagen o ejecutar la aplicación.

## Estructura del proyecto

- `streamlit.py` — punto de entrada de la aplicación y navegación
- `model_demonstration.py` — página principal: subida de imágenes, predicciones, tabla de resultados, curvas de entrenamiento
- `translations.py` — diccionarios de textos de la interfaz para ucraniano, inglés y español
- `functions.py` — funciones auxiliares (por ejemplo, graficar las curvas de entrenamiento)
- `requirements.txt` — dependencias directas del proyecto
- `Dockerfile` — definición de la construcción del contenedor

## Conclusión

El modelo VGG16 con fine-tuning alcanzó un 92.41% — ligeramente mejor que la CNN propia (91.83%), aunque sin una mejora drástica. Inicialmente, con la base completamente congelada, la precisión se mantenía alrededor del 85%. Tras descongelar los bloques 4 y 5 con una tasa de aprendizaje muy baja, la precisión subió hasta 92.41% — es decir, el fine-tuning por sí solo aportó casi 7 puntos porcentuales de mejora.
