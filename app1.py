from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store quotations for each mode
quotations = {
    'happy': "The only way to be happy is to love. Unless you love, your life will flash by.",
    'sad': "The greatest joy in life is to love and be loved in return.",
    'excited': "The best way to predict the future is to create it."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mode = request.form['mode'].lower()
        quotation = quotations.get(mode, 'Invalid mode entered. Please try again.')
        return jsonify({'quotation': quotation})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
