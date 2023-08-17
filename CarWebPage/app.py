from flask import Flask, request, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

# Initial values
doors_locked = "Locked"
windows_status = "Closed"
engine_status = "Off"
range_value = "350 Miles"
gas = "90%"
system_status = "Working"

@app.route('/', methods=['GET', 'POST'])
def index():
    global doors_locked, windows_status, engine_status, range_value, gas, system_status
    
    if request.method == 'POST':
        data = request.get_json()
        if data:
            doors_locked = data.get('doors_locked', doors_locked)
            windows_status = data.get('windows_status', windows_status)
            engine_status = data.get('engine_status', engine_status)
            range_value = data.get('range_value', range_value)
            gas = data.get('gas', gas)
            system_status = data.get('system_status', system_status)
            
            return "Values updated successfully!"
    
    current_values = {
        'doors_locked': doors_locked,
        'windows_status': windows_status,
        'engine_status': engine_status,
        'range_value': range_value,
        'Charge': gas,
        'system_status': system_status
    }
    
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(current_values)
    else:
        return render_template('index.html', doors_locked=doors_locked, windows_status=windows_status,
                               engine_status=engine_status, range_value=range_value, gas=gas,
                               system_status=system_status)

@app.route('/static/<filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
