from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    return jsonify({"message": "🎉 Ticket Booked Successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=7000)
