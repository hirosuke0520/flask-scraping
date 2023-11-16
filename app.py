from flask import Flask, request, jsonify
from tiktok_scraping import get_tiktok_profile_by_selenium, fuga
from wsgiref.handlers import CGIHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "flask-scraping"

@app.route('/get_profile', methods=['GET'])
def get_profile():
    user_ids = request.args.get('user_ids').split(',')  # カンマ区切りのuser_idを分割
    profiles = [get_tiktok_profile_by_selenium(user_id) for user_id in user_ids]
    return jsonify(profiles)

@app.route('/hoge', methods=['GET'])
def hoge():
    return fuga()

if __name__ == '__main__':
    app.run(debug=True)

# CGI環境での実行用に変更
# CGIHandler().run(app)