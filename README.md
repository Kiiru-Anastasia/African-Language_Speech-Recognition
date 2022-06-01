# African Language Speech Recognition
## Speech-to-Text with Deep Learning

### Business Scenario
****
The World Food Program wants to deploy an intelligent form that collects nutritional information of food bought and sold at markets in two different countries in Africa - Ethiopi and Kenya.
The design of this intelligent form requires selected people to install an app on their mobile phone and whenever they buy food they use their voice to activate the app to register the list of items they just bought in their own language.
The intelligent systems in the app are expected to live transcribe the speech-to-text and organize the information in an easy-to-process way in a database.

**Objective:** Build a deep learnin model that is capable of transcribing a speech to text. The model should be accurate and robust against background noise.

### Data Features
****
* Input features(X): audio clips of spoken words
* Target labels(y): a text transcript of what was spoken

### Project Outcomes
****
#### Skills:
* Working with audio and text files
* Familiarity with deep learning architecture
* Model management(building ML catalog containing models, feature labels, and training model version)
* Comparing multiple Deep Learning techniques.
* Training and validating DL models
* Choosing appropriate architecture, loss function and regularisers, hyperparameter tuning, and choosing suitable evaluation metrics
* MLOps with DVC, CML, and MLflow

#### Knowledge:
* Audio and text processing
* Deep learning methods (TensorFlow, Keras, Pytorch)
* Hyperparameter tuning
* Model comparison & selection
* Experiment Analysis

### Steps followed in Project
****
1. Business and Data Understanding
2. Repository setup: DVC, MLflow and CML integration
3. Data exploration, visualization, transformation, and augmentation
4. Choosing and implementing Deep Learning architecture, loss funciton, evaluation metrics, and other necessary variables
5. Training, Testing and Evaluation (Understanding effect of hyperparameters)
6. Model deployment to an easy-to-use dashboard.
7. Model deployment as a skill for Amazon Alexa

### Project Structure
****
The structure and brief explanation for the repository.

**.dvc:**

* contains data versioning setup and version storage

**.github/workflows:**

* contains workflows to ensure CI/CD

**mlruns/0:**

* model artifacts

**models:**

* trained DL models

**notebooks:**

jupyter notebook files

* audio_overview.ipynb - an overview of a single audio file. Waveplots and playbacks
* metadata_generator.ipynb - creates the dataframe with metadata for audio files. filename, transcription, filepath, sample rate and duration.

**scripts:**

helper functions

* audio_overview.py - script file used in audio_overview notebook

**tests:**
* unittests

**root folder**

Any other aditional files

* .dvcignore
* .gitignore
* README.me

### Installation guide
****