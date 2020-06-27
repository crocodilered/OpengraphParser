"""
Small service to get page URL as input and return list of OpenGraph tags found in that page.
"""

from flask import Flask, request, Response, jsonify, g, json
from flask_cors import CORS
from requests import Session

from libs.og_parser import OgParser


app = Flask(__name__)
CORS(app)


def get_session() -> Session:
    """
    Get app context variable with requests session.
    :return: Requests Session object.
    """
    if 'session' not in g:
        g.session = Session()

    return g.session


def get_parser() -> OgParser:
    """
    Get app context variable with OG parser.
    :return: Parser object.
    :return:
    """
    if 'parser' not in g:
        g.parser = OgParser()

    return g.parser


def error(code, message: str = '') -> Response:
    """
    Make response with error.
    :param code: Error code.
    :param message: Error message (optional).
    :return: Complete Response object with given code and optional message.
    """
    ret = {'code': code}

    if message != '':
        ret['message'] = message

    return Response(
        response=json.dumps(ret),
        status=400,
        content_type='application/json'
    )


@app.route('/', methods=['POST'])
def index() -> Response:
    """
    Find page by given URL and return OpenGraph tags found.
    Can fire errors:
         - param-expected: no URL param given,
         - page-unavailable: page with given URL is not available.
    :return: OpenGraph tags found
    """
    url = request.json.get('url')

    if url is None:
        return error('param-expected', '@url param expected.')

    sess = get_session()
    resp = sess.get(url)

    if resp.status_code != 200:
        return error(
            'page-unavailable',
            'Page with given URL is not available (got HTTP 404 error).'
        )

    parser = get_parser()
    ret = parser.exec(resp.text)

    return jsonify(ret)


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
