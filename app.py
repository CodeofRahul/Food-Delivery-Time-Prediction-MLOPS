from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import DataIngestion
from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import CustomData, PredictionPipeline
from werkzeug.utils import secure_filename
from Prediction.batch import *
from src.pipeline.training_pipeline import Train

feature_engineering_file_path = FEATURE_ENGG_OBJ_PATH
transformer_file_path = PREPROCESSING_OBJ_FILE
model_file_path = MODEL_FILE_PATH

UPLOAD_FOLDER = "batch_Prediction/UPLOADED_CSV_FILE"

app = Flask(__name__, template_folder = "templates")

ALLOWED_EXTENSIONS = {'csv'}

# localhost:5000
@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/predict', methods = ['GET', 'POST'])


def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            Delivery_Person_Age = int(request.form.get('Delivery_Persom_Age')),
            Delivery_Person_Ratings = float(request.form.get('Delivery_Person_Ratings')),
            Weather_conditions = request.form.get('Weather_conditions'),
            Road_traffic_density = request.form.get('Road_traffic_density'),
            Vehicle_condition = int(request.form.get('Vehicle_condition')),
            multiple_deliveries = int(request.form.get('multiple_deliveries')),
            distance = float(request.form.get('distance')),
            Type_of_order = request.form.get('Type_of_order'),
            Type_of_vehicle = request.form.get('Type_of_vehicle'),
            Festival = request.form.get('Festival'),
            City = request.form.get('City')
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = predict_pipeline()
        pred = predict_pipeline.predict(final_new_data)

        result = int(pred[0])

        return render_template('form.html', final_result=result)
    

@app.route("/batch", methods = ['GET', 'POST'])
def perform_batch_prediction():


    if request.method == 'GET':
        return render_template('batch.html')
    else:
        file = request.files['csv_file']       # Update the key to 'csv file'
        # Directory path
        directory_path = UPLOAD_FOLDER
        # create the directory
        os.makedirs(directory_path, exist_ok=True)

        # Check if the file has a valid extension
        if file and '.' in file.filename and file.filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            # Delete all files in the file path
            for filename in os.listdir(os.path.join(UPLOAD_FOLDER)):
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

            # Save the new file to the uploads directory
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            print(file_path)

            logging.info("CSV received and Upload")

            # Perform batch prediction using the upload file
            batch = batch_prediction(file_path,
                                     model_file_path,
                                     transformer_file_path,
                                     feature_engineering_file_path)
            batch.start_batch_prediction()

            output = "Batch Prediction Done"
            return render_template("batch.html", prediction_result=output, prediction_type='batch')
        else:
            return render_template("batch.html", prediction_type='batch', error='Invalid file type')
        

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'GET':
        return render_template('train.html')
    else:
        try:
            Pipeline = Train()
            Pipeline.main()

            return render_template('train.html', message='Training complete')
        
        except Exception as e:
            logging.error(f"{e}")
            error_message = str(e)
            return render_template('index.html', error = error_message)
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='8888')