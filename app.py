from flask import Flask, jsonify, request
from functions import pdf_rotation


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def help():
    if(request.method == 'GET'):
        data = {
            'rotate':
            {
                'parameters':
                {
                    'angle': 'Angle to be roated to',
                    'page': 'Page no of page to be rotated',
                    'path': 'Filepath of pdf file'
                },
                'example': 'http://127.0.0.1:5000/rotate?angle=90&page=1&filepath=C:/Users/sample.pdf'
            }
        }
        return jsonify(data)


@app.route('/rotate', methods=['GET'])
def rotate():
    args = request.args
    args.get("angle", type=int)
    args.get("page", type=int)
    args.get("filepath", type=str)
    return pdf_rotation(int(args['angle']), int(args['page']), args['filepath'])


if __name__ == '__main__':
    app.run(debug=True)
