from flask import Flask, jsonify, request
import functions
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def help():
    if(request.method == 'GET'):
        _file = 'help.json'
        with open(_file, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return jsonify(data)


@app.route('/rotate', methods=['GET'])
def rotate():
    args = request.args
    args.get("angle", type=int)
    args.get("page", type=int)
    args.get("filepath", type=str)
    return functions.pdf_rotation(int(args['angle']),
                                  int(args['page']),
                                  args['filepath'])


@app.route('/merge', methods=['GET'])
def merge():
    args = request.args
    args.get("pdf_loc", type=list)
    args.get("save_loc", type=str)
    args.get("save_pdf", type=str)
    if args['save_pdf'] != "":
        return functions.pdf_merge(args['pdf_loc'], args['save_loc'], args['save_pdf'])
    return functions.pdf_merge(args['pdf_loc'], args['save_loc'])


if __name__ == '__main__':
    app.run(debug=True)
