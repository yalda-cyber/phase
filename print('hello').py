from flask import Flask, request, render_template_string
import pandas as pd

temperature_data = pd.DataFrame({
    'Temperature': [0.01, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 374.1],
    'Pressure': [0.6113, 0.8721, 1.2276, 1.705, 2.339, 3.169, 4.246, 5.628, 7.384, 9.593, 12.35, 15.758, 19.941, 25.03, 31.19, 38.58, 47.39, 57.83, 70.14, 84.55, 101.3, 120.8, 143.3, 169.1, 198.5, 232.1, 270.1, 313.0, 361.3, 415.4, 475.9, 543.1, 617.8, 700.5, 791.7, 892.0, 1002.2, 1122.7, 1254.4, 1397.8, 1553.8, 1723.0, 1906.3, 2104.2, 2317.8, 2547.7, 2794.9, 3060.1, 3344.2, 3648.2, 3973.0, 4319.5, 4688.6, 5081.3, 5498.7, 5941.8, 6411.7, 6909.4, 7436.0, 7992.8, 8581.0, 9201.8, 9856.6, 10547.0, 11274.0, 12040.0, 12845.0, 13694.0, 14586.0, 15525.0, 16514.0, 17554.0, 18651.0, 19807.0, 21028.0, 22089.0]
})

pressure_data = pd.DataFrame({
    'Pressure': [0.6113, 0.8721, 1.2276, 1.705, 2.339, 3.169, 4.246, 5.628, 7.384, 9.593, 12.35, 15.758, 19.941, 25.03, 31.19, 38.58, 47.39, 57.83, 70.14, 84.55, 101.3, 120.8, 143.3, 169.1, 198.5, 232.1, 270.1, 313.0, 361.3, 415.4, 475.9, 543.1, 617.8, 700.5, 791.7, 892.0, 1002.2, 1122.7, 1254.4, 1397.8, 1553.8, 1723.0, 1906.3, 2104.2, 2317.8, 2547.7, 2794.9, 3060.1, 3344.2, 3648.2, 3973.0, 4319.5, 4688.6, 5081.3, 5498.7, 5941.8, 6411.7, 6909.4, 7436.0, 7992.8, 8581.0, 9201.8, 9856.6, 10547.0, 11274.0, 12040.0, 12845.0, 13694.0, 14586.0, 15525.0, 16514.0, 17554.0, 18651.0, 19807.0, 21028.0, 22089.0],
    'Temperature': [0.01, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 105.0, 110.0, 115.0, 120.0, 125.0, 130.0, 135.0, 140.0, 145.0, 150.0, 155.0, 160.0, 165.0, 170.0, 175.0, 180.0, 185.0, 190.0, 195.0, 200.0, 205.0, 210.0, 215.0, 220.0, 225.0, 230.0, 235.0, 240.0, 245.0, 250.0, 255.0, 260.0, 265.0, 270.0, 275.0, 280.0, 285.0, 290.0, 295.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 355.0, 360.0, 365.0, 370.0, 374.1]
})

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phase Detector</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h1 class="text-center text-primary">Phase Detector</h1>
    <form method="post" class="mt-4">
        <div class="mb-3">
            <label for="temperature" class="form-label">Temperature (°C):</label>
            <input type="number" step="any" id="temperature" name="temperature" class="form-control" required>
        </div>
        <div class="mb-3">
            <label for="pressure" class="form-label">Pressure (KPa):</label>
            <input type="number" step="any" id="pressure" name="pressure" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Comparison Type:</label><br>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="compare_type" id="temperature_radio" value="temperature" checked>
                <label class="form-check-label" for="temperature_radio">Temperature</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="compare_type" id="pressure_radio" value="pressure">
                <label class="form-check-label" for="pressure_radio">Pressure</label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Check Phase</button>
    </form>

    {% if result %}
        <div class="alert alert-info mt-4" role="alert">
            {{ result }}
        </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def phase_detector():
    result = None
    if request.method == 'POST':
        try:
            temperature = float(request.form['temperature'])
            pressure = float(request.form['pressure'])
            compare_type = request.form['compare_type']

            if compare_type == "temperature":
                sat_data = temperature_data[temperature_data['Temperature'] == temperature]
                if not sat_data.empty:
                    sat_pressure = sat_data['Pressure'].iloc[0]
                    if pressure > sat_pressure:
                        result = "Phase: Compressed liquid"
                    elif pressure < sat_pressure:
                        result = "Phase: Superheated vapor"
                    else:
                        result = "Phase: Two-phase mixture"
                else:
                    result = "Temperature out of range of the table."

            elif compare_type == "pressure":
                sat_data = pressure_data[pressure_data['Pressure'] == pressure]
                if not sat_data.empty:
                    sat_temperature = sat_data['Temperature'].iloc[0]
                    if temperature < sat_temperature:
                        result = "Phase: Compressed liquid"
                    elif temperature > sat_temperature:
                        result = "Phase: Superheated vapor"
                    else:
                        result = "Phase: Two-phase mixture"
                else:
                    result = "Pressure out of range of the table."

        except ValueError:
            result = "Invalid input. Please enter numeric values."

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
