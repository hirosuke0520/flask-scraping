from flask import Flask, request, jsonify
from tiktok_scraping import get_tiktok_profile_by_selenium

app = Flask(__name__)

@app.route('/get_profile', methods=['GET'])
def get_profile():
    user_ids = request.args.get('user_ids').split(',')  # カンマ区切りのuser_idを分割
    profiles = [get_tiktok_profile_by_selenium(user_id) for user_id in user_ids]
    return jsonify(profiles)

if __name__ == '__main__':
    app.run()
