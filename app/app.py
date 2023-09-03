import json
import pandas as pd
from flask import Flask, jsonify, request, render_template
from utils import predict_approval
import datetime
import config
from flask_cors import CORS
import sys
sys.path.append('../pipelines/')
from etl.config import COURSE_NAMES
from models.config import FEATURES

app = Flask(__name__, template_folder='template', static_folder='template/assets')
CORS(app)

#df_scores = pd.read_parquet('../data/processed/scores_approvals_convocation_2020_2022.parquet')
#df_scores = df_scores[config.RESULTS_INFO]

# @app.route('/filter', methods=['GET']) 
# def filter_dataframe():
#     numero_inscricao = request.args.get('numero_inscricao')  # Get 'name' parameter from the request

#     if numero_inscricao:
#         filtered_df = df_scores[df_scores['numero_inscricao'] == numero_inscricao]  # Filter DataFrame based on 'name'
#         result = filtered_df.to_dict('records')
#     else:
#         result = df_scores.to_dict('records')  # Return the entire DataFrame if 'name' parameter is not provided

#     return jsonify(result)

@app.route('/')
def form_page():
    data = {
        'features': FEATURES,
        'course_names' : COURSE_NAMES
    }
    return render_template('formpage.html', data=data)

@app.route('/result')
def result():
    data = {
        'escore_bruto_p1_etapa1': float(request.args.get('escore_bruto_p1_etapa1')),
        'escore_bruto_p2_etapa1': float(request.args.get('escore_bruto_p2_etapa1')),
        'escore_bruto_p1_etapa2': float(request.args.get('escore_bruto_p1_etapa2')),
        'escore_bruto_p2_etapa2': float(request.args.get('escore_bruto_p2_etapa2')),
        'escore_bruto_p1_etapa3': float(request.args.get('escore_bruto_p1_etapa3')),
        'escore_bruto_p2_etapa3': float(request.args.get('escore_bruto_p2_etapa3')),
        'cotas_negros_flag': int(request.args.get('cotas_negros_flag')),
        'publicas1_flag': int(request.args.get('publicas1_flag')),
        'publicas2_flag': int(request.args.get('publicas2_flag')),
        'publicas3_flag': int(request.args.get('publicas3_flag')),
        'publicas4_flag': int(request.args.get('publicas4_flag')),
        'publicas5_flag': int(request.args.get('publicas5_flag')),
        'publicas6_flag': int(request.args.get('publicas6_flag')),
        'publicas7_flag': int(request.args.get('publicas7_flag')),
        'publicas8_flag': int(request.args.get('publicas8_flag')),
        'course': request.args.get('course'),
    }

    approval_prediction = predict_approval(data)

    result_data = {
        'approval_prediction': approval_prediction
    }
        
    return render_template('resultpage.html', data=result_data)

@app.post('/predict') 
def predict():
    
    # this is a python dictionary 
    data = request.json
           
    approval_prediction = predict_approval(data)
        
    try:
        result = jsonify({'metadata': {"timestamp": str(datetime.datetime.now())},
                          'prediction': {"probability": approval_prediction}})
    
    except TypeError as e:
        return jsonify({'error': str(e)})
        
    return result
    

if __name__ == '__main__':
    app.run(debug=True)
