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


@app.route('/generator/v1.0/diploma', methods=['POST'])
def generate_diplomas():
    # if there is no json at all or not all mandatory data are posted
    required_fields = ['template', 'data']
    if not request.json or \
            not all(field in request.json for field in required_fields):
        return make_response("Wrong request data", 400)
    else:
        if 'output_file_type' not in request.json:
            output_file_type = 'docx'
        else:
            output_file_type = request.json['output_file_type']

        user_filename = datetime.now().strftime("%Y-%m-%d") + "_certyfikaty.docx"
        generator = Generator(request.json['template'])
        if output_file_type == 'docx':
            file_path=generator.get_docx_file(request.json['data'])
        else:
            return make_response("Unsupported output type", 400)

        split_path = os.path.split(file_path)
        return send_from_directory(directory=split_path[0], filename=split_path[1],
                                   as_attachment=True, attachment_filename=user_filename)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
