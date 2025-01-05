from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Task targets dictionary
task_targets = {
    "Explicit Lane Lines Lane Adjacencies": 1.87,
    "Explicit Lane Lines Lane Adjacencies QA 3D": 4.52,
    "Navigable Boundaries Legacy": 2.72,
    "Navigable Boundaries QA 3D Legacy": 2.61,
    "Intersection Zoi Legacy": 1.5,
    "Intersection Zoi QA 2D Legacy": 2,
    "Road Paint Zois Legacy": 3.05,
    "Road Paint Zois QA 3D Legacy": 3.94,
    "Legacy Signs Speed Limit Values Sign Associations": 3,
    "Legacy Signs Speed Limit Values Sign Associations 3D": 4,
    "Legacy QA 3D": 1.5  # Corrected value
}

@app.route('/')
def index():
    return render_template('index.html')  # Ensure the HTML file is named index.html

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Ensure the data contains at least one task
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Calculate the total target achieved
    total_target_achieved = 0.0
    for task, km in data.items():
        if task in task_targets:
            total_target_achieved += km / (task_targets[task] * 8)  # Assuming 8 hours work per task
    
    target_percentage = total_target_achieved * 100

    return jsonify({'achieved': f"{target_percentage:.2f}%"})

if __name__ == '__main__':
    app.run(debug=True)
