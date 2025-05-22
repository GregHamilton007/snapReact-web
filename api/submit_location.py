from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

SUBMISSIONS_FILE = 'location_submissions.json'

def load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_submissions(submissions):
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(submissions, f, indent=2)

@app.route('/api/submit-location', methods=['POST'])
def submit_location():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['address', 'mode', 'reason']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Create submission object
        submission = {
            'address': data['address'],
            'mode': data['mode'],
            'reason': data['reason'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Load existing submissions
        submissions = load_submissions()
        
        # Add new submission
        submissions.append(submission)
        
        # Save updated submissions
        save_submissions(submissions)
        
        return jsonify({'message': 'Location submitted successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/view-submissions', methods=['GET'])
def view_submissions():
    try:
        submissions = load_submissions()
        return jsonify(submissions), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 