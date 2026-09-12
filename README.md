# deep_learning_clothing_classifier
Image classification on Fashion-MNIST comparing a custom CNN (91.83% accuracy) against fine-tuned VGG16 transfer learning (92.41% accuracy), with data augmentation, EarlyStopping, and learning-rate scheduling. Includes a Streamlit app for uploading images and viewing live predictions with confidence scores and training curves.


### Model Weights Setup
1. Download the model weights from [this Google Drive link](https://drive.google.com/file/d/1UXVYjxOxjt-ZB0cezdNeXF2-K3Bvxp5X/view?usp=sharing).
2. Place `vgg16_model.keras` into the root project directory before running the Streamlit app.