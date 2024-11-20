import joblib
import pandas as pd
from flask import Flask, request, jsonify
import os 
from dotenv import load_dotenv
load_dotenv() 
app = Flask(__name__)

model_path = os.getenv('MODEL_PATH', 'modelo.pkl')
prepoc_path = os.getenv('PREPROCESSOR_PATH', 'preprocesador.pkl')
print(f"Ruta del modelo: {model_path}")
print(f"Ruta del preprocesador: {prepoc_path}")

model = joblib.load(model_path)
preprocessor = joblib.load(prepoc_path)

@app.route('/')
def home():
    return "API de predicción de ventas de entradas"

@app.route('/predecir', methods=['POST'])
def predecir():
    try:
        # Obtener datos JSON enviados en la solicitud
        data = request.json
        
        # Convertir a DataFrame de pandas para procesar
        df = pd.DataFrame([data])

        # Preprocesar los datos
        datos_preprocesados = preprocessor.transform(df)

        # Hacer la predicción
        prediccion = model.predict(datos_preprocesados)

        # Devolver la predicción como JSON
        return jsonify({
            'prediccion': round(prediccion[0], 0)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ejecuta siempre en el puerto 5000