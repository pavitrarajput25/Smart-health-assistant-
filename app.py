from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def dashboard():
    # In a real app, fetch vitals from a database
    vitals = {"temp": 37.1, "pulse": 82}
    return render_template('index.html', vitals=vitals)

@app.route('/analyze-skin', methods=['POST'])
def analyze_skin():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    # Placeholder for AI Model Processing logic
    # result = model.predict(file)
    
    return jsonify({
        "status": "Success",
        "analysis": "No significant irregularities detected. Consult a doctor if redness persists."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
