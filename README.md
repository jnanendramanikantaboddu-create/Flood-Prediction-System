                         🌊 RISING WATERS: FLOOD PREDICTION SYSTEM
                     A Machine Learning Based Approach for Early Flood Risk Detection


1. Project Description

The Rising Waters: Flood Prediction System is a machine learning-based application designed to predict the likelihood of flood occurrence using environmental and geographical parameters.
Floods are among the most destructive natural disasters, causing significant damage to human life, infrastructure, and agriculture. Early prediction and risk assessment are essential to minimize losses.
This project analyzes historical flood-related data such as rainfall intensity, deforestation levels, urbanization rate, drainage conditions, and river management factors. Using this data, a Random Forest Classifier model is trained to predict whether flood conditions are likely or not.
The trained model is deployed using Flask to provide a simple web interface where users can enter environmental parameters and receive real-time flood predictions.



3. Project Demo Video
   
Due to GitHub preview limitations, the demo video can be downloaded using the link below:
Download Demo Video:
https://github.com/jnanendramanikantaboddu-create/Flood-Prediction-System/raw/main/demo%20video.mp4



5. Team Details
   
Team ID: LTVIP2026TMIDS90596
Team Leader:

Peddina Supraja

Team Members:

Jnanendra Manikanta Boddu

Meghana Buddepu

Manasa Ratna Redl

7. Project Structure:

Entity	Type	Description
data/	Directory	Contains flood.csv; the raw dataset used for training and testing.
static/	Directory	Stores static assets like style.css for the web interface.
templates/	Directory	Contains index.html; the frontend UI rendered by the Flask app.
app.py	Script	The main application file that handles web requests and model inference.
train_model.py	Script	Python script used to preprocess data and train the machine learning model.
flood_model.pkl	Model	The serialized (saved) version of your trained model, ready for prediction.
Flood_Prediction_Model.ipynb	Notebook	Interactive Jupyter notebook for Exploratory Data Analysis (EDA) and prototyping.
requirements.txt	Config	List of all Python libraries (scikit-learn, pandas, flask) needed to run the project.
demo_video.mp4	Media	A screen recording demonstrating the system's functionality.
README.md	Documentation	The primary guide for setup, installation, and project overview.



9. Technologies Used
    

Language: Python

Machine Learning Libraries:

•	NumPy

•	Pandas

•	Scikit-learn

Visualization:

•	Matplotlib

•	Seaborn

Model:

•	Random Forest Classifier

Web Framework:

•	Flask

Frontend:

•	HTML

•	CSS

Model Serialization:

•	Joblib / Pickle

Development Environment:

•	Jupyter Notebook

•	VS Code

6. Methodology
   
The project follows these steps:

1.	Data Collection

Historical flood-related dataset is collected.

2.	Data Preprocessing

o	Handling missing values

o	Feature selection

o	Data splitting into training and testing sets

3.	Model Building

Random Forest Classifier is used for training the model.

4.	Model Evaluation

Accuracy score and confusion matrix are calculated.

5.	Model Deployment

The trained model is integrated into a Flask web application.

7. Project Setup 

To get this system running on your local machine, follow these steps in order:

Phase 1: Environment Preparation

Step	Action	Command

1	Clone Repository	git clone https://github.com/jnanendramanikantaboddu-create/Flood-Prediction-System.git


2	Initialize Virtual Env	python -m venv .venv

3	Activate Environment	Win: .venv\Scripts\activateUnix: source .venv/bin/activate

Phase 2: Installation & Execution

1.	Install Dependencies Ensure all required ML and Web libraries are present

(pip install numpy pandas matplotlib seaborn scikit-learn flask joblib) 

2.Train the Intelligence Run the training script to generate the flood_model.pkl file:
                 (python train_model.py)
3.Launch the Portal Start the Flask server:
                (python app.py) 
 
 Access Point: Open your browser and navigate to http://127.0.0.1:5000

8. Results & Performance 📊

The Rising Waters system was evaluated based on historical environmental parameters.

•	Model Accuracy: The Random Forest Classifier was selected for its robust handling of non-linear environmental data, achieving high precision in flood vs. no-flood classification.

•	User Experience: The web interface provides instant inference, allowing users to input parameters and receive a prediction in under 200ms.

•	Data Visualization: The system generates correlation heatmaps and trend analysis, making complex environmental data easy to digest.

9. Conclusion & Future Roadmap 🏁

This project demonstrates the synergy between Machine Learning and Disaster Risk Management. By leveraging predictive analytics, we can transform reactive disaster response into proactive preventive action.

Key Takeaways

•	Early Detection: Provides a critical window for evacuation and resource allocation.

•	Accessibility: A lightweight Flask UI ensures the tool is usable by non-technical authorities.
The Road Ahead

•	📡 Live Integration: Connecting to real-time OpenWeather APIs for automated predictions.

•	☁️ Cloud Deployment: Moving from local hosting to AWS or Azure for global availability.

•	🧠 Deep Learning: Implementing LSTMs (Long Short-Term Memory) to better handle time-series weather data.



