from flask import Flask, jsonify, make_response, send_from_directory, request
from generator import Generator
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/generator/v1.0/templates', methods=['GET'])
def get_templates():
    templates = []
    for file in os.listdir(Generator.template_folder_name):
        if file.endswith(".docx"):
            templates.append(file)
    return jsonify({'templates': templates})


@app.route('/generator/v1.0/diploma', methods=['GET', 'POST'])
def generate_diplomas():
    filename = datetime.now().strftime("%Y-%m-%d") + "_certyfikaty.docx"
    generator = Generator("cert_kurs_template.docx")
    # TODO get data from json request
    generator.marge_pages_to_file(Generator.sample_data, filename)
    return send_from_directory(directory=Generator.temp_files_folder_name, filename=filename,
                               as_attachment=True, attachment_filename=filename)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
