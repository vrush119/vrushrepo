from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    # Save the file (you can customize the save path)
    file.save(f'uploads/{file.filename}')
    return f'File {file.filename} uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
