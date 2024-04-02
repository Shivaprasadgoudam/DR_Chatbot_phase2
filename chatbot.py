from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set your Google API key here
GOOGLE_API_KEY = 'GOOGLE_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Route for rendering index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for rendering hospital.html
@app.route('/hospital')
def hospital():
    return render_template('hospital.html')

# Route for chatbot API endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    symptoms = data.get('symptoms', '')
    kl = "I have the symptoms of "
    lk = " which disease is this? and give description of identified disease and precautions, don't give medicine advice"
    try:
        response = model.generate_content(kl + symptoms + lk)
        return jsonify({'message': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
