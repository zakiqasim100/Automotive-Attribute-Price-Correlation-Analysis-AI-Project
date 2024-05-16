from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():
    return render_template('upload.html')

# Define the route for handling file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        file_path = 'uploads/' + file.filename
        file.save(file_path)
        return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
