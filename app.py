from flask import Flask, session, url_for ,render_template, make_response ,request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.debug('index called...')
    resp = make_response(render_template('index.html'))
    return resp

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

with app.test_request_context():
    print(url_for('index'))
    print(url_for('static', filename='css/all.min.css'))
