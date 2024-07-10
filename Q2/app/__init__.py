from flask import Flask, request, jsonify
import pickle
import logging

app = Flask(__name__)

# logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

# load the model
def load_model():
    try:
        model = pickle.load(open('final_model.pkl', 'rb'))
        logging.info('Model loaded successfully')
        return model
    except Exception as e:
        logging.error(f'Failed to load model: {str(e)}')
        raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # get data from request
        data = request.get_json()

        # load the model
        model = load_model()

        # perform prediction using your model
        prediction = model.predict(data['input_data'])

        # prepare response
        response = {'prediction': prediction}

        return jsonify(response), 200

    except Exception as e:
        error_msg = f'Prediction error: {str(e)}'
        logging.error(error_msg)
        return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
