# deep_learning_clothing_classifier

Image classification on Fashion-MNIST comparing a custom CNN (91.83% accuracy) against fine-tuned VGG16 transfer learning (92.41% accuracy), with data augmentation, EarlyStopping, and learning-rate scheduling. Includes a Streamlit app for uploading images and viewing live predictions with confidence scores and training curves.

The app supports both **Ukrainian** and **English** interfaces, switchable from the sidebar.

## Model Weights Setup

1. Download the model weights from [this Google Drive link](https://drive.google.com/file/d/1UXVYjxOxjt-ZB0cezdNeXF2-K3Bvxp5X/view?usp=sharing).
2. Place `vgg16_model.keras` into the root project directory before running the Streamlit app.

## Running Locally

```bash
conda activate clothing_classifier
streamlit run streamlit.py
```

The app will be available at `http://localhost:8501` (or whichever port Streamlit reports in the terminal).

## Running with Docker

Build the image:

```bash
docker build . -t clothing-classifier
```

Run the container:

```bash
docker run --name clothing-classification-app -p 8500:8501 -d clothing-classifier
```

The app will be available at `http://localhost:8500`.

To view logs:

```bash
docker logs clothing-classification-app
```

To stop the container:

```bash
docker stop clothing-classification-app
```

> **Note:** the trained `.keras` model files are not included in this repository or in the Docker build context due to their size. Make sure they are present in the project root (see *Model Weights Setup* above) before building the image or running the app.

## Project Structure

- `streamlit.py` — app entry point and navigation
- `model_demonstration.py` — main page: image upload, predictions, results table, training curves
- `translations.py` — UI text dictionaries for Ukrainian and English
- `functions.py` — helper functions (e.g., training curve plotting)
- `requirements.txt` — direct project dependencies
- `Dockerfile` — container build definition

## Conclusion

The VGG16 model with fine-tuning achieved 92.41% — slightly better than the custom CNN (91.83%), but not a dramatic improvement. Initially, with the base model completely frozen, accuracy hovered around 85%. After unfreezing blocks 4 and 5 with a very low learning rate, accuracy rose to 92.41% — meaning fine-tuning alone contributed nearly 7 percentage points of improvement.
