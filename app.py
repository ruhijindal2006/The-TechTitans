# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     crop = request.form['crop']
#     print(f"Farmer: {name}, Crop: {crop}")
#     return f"Received submission from {name} with crop: {crop}"

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from utils.ndvi_fetcher import get_ndvi
from utils.soil_data import get_soil_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    lat = float(request.form['latitude'])
    lon = float(request.form['longitude'])

    ndvi_score = get_ndvi(lat, lon)
    soil_info = get_soil_data(lat, lon)

    # Simple decision logic
    if ndvi_score < 0.3:
        crop_suggestion = "Sorghum or Millet (drought resistant)"
    else:
        crop_suggestion = "Wheat or Rice"

    return jsonify({
        'ndvi': ndvi_score,
        'soil': soil_info,
        'suggested_crop': crop_suggestion
    })

if __name__ == '__main__':
    app.run(debug=True)
