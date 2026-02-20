         Rising Waters: Flood Prediction System 🌊
Objective :
             This project aims to predict the likelihood of floods in Kerala based on monthly rainfall data using Machine Learning.


A) Technical Stack

Language : 
              Python 3.x

2. Libraries :
              Pandas, NumPy, Scikit-Learn, Flask, Joblib

3. Algorithm : 
              Random Forest Classifier

4. Deployment :
              Flask Web Framework

B) Project Workflow :

Data Collection :
                   Used the kerala.csv dataset containing historical rainfall records.

2. Pre-processing :
                  Handled categorical labels by mapping "YES/NO" flood outcomes to numerical values (1/0).

3. Model Building : 
                  Trained a Random Forest Classifier to identify patterns in rainfall intensity across 12 months.

4. Saving Model : 
                 Exported the trained brain as flood_model.pkl for real-time use.

5. Web Deployment :
                   Built a Flask interface (app.py) where users can input rainfall data to get an instant prediction.