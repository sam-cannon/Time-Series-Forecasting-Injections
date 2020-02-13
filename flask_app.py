import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle
import datetime as dt
import os

# app
app = Flask(__name__)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.path.join(THIS_FOLDER, 'final_prophet_model.sav', 'rb')

# load model
model = pickle.load(open('/home/samcannon/mysite/final_prophet_model.sav','rb'))


@app.route('/')
def home():
    return render_template('index_3.html')

# routes
@app.route('/predict', methods=['POST'])

def predict():

    # get data from form
    date = [x for x in request.form.values()]

    #convert data to df for prophet to predict
    prediction_df = pd.DataFrame({'ds':[dt.datetime.strptime(date, '"%Y-%m-%d"').date() for date in date]})

    # predictions
    prediction = model.predict(prediction_df)

    # send back to browser
    output = int(prediction.iloc[:, -1])

    # return data
    return render_template('index_3.html', prediction_text=f'There will be around {output} injections')

@app.route('/results',methods=['POST'])

def results():

    data = request.get_json(force=True)

    #convert data into df
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    #predictions
    result = model.predict(data_df)

    #output
    output = {'results': int(result.iloc[:, -1])}

    return jsonify(output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)