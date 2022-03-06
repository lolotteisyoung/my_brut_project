from flask import Flask, request, jsonify
import my_operator
from datetime import datetime
from my_database import create_tables

app = Flask(__name__)


@app.route('/pages', methods=["GET"])
def get_pages():
    pages = my_operator.get_pages()
    return jsonify(pages)


@app.route('/videos', methods=["GET"])
def get_videos():
    videos = my_operator.get_videos()
    return jsonify(videos)


@app.route('/insights', methods=["GET"])
def get_insights():
    insights = my_operator.get_insights()
    return jsonify(insights)


@app.route('/insights/<id>', methods=["GET"])
def get_insights_by_video_id(id):
    insights = my_operator.get_insights_by_video(id)
    return jsonify(insights)


@app.route('/page', methods=["POST"])
def add_page():
    page_info = request.get_json()


@app.route('/video', methods=["POST"])
def add_video():
    video_info = request.get_json()


@app.route('/insight', methods=["POST"])
def add_insight():
    insight_info = request.get_json()


@app.route("/page/<id>", methods=["DELETE"])
def delete_page(id):
    action = my_operator.delete_page(id)
    return jsonify(action)


@app.route("/video/<id>", methods=["DELETE"])
def delete_video(id):
    action = my_operator.delete_page(id)
    return jsonify(action)


@app.route("/insight/<id>", methods=["DELETE"])
def delete_insight(id):
    action = my_operator.delete_insight(id)
    return jsonify(action)


page = {
    'created_at': datetime.now(),
    'page_id': 70515,
    'page_name': 'Our Media France'
}
video_a = {
    'created_at': datetime.now(),
    'video_id': 33401,
    'video_title': 'Parlons Cash',
    'page_id': 70501,
}
video_b = {
    'created_at': datetime.now(),
    'video_id': 33401,
    'video_title': "Privés d'écran",
    'page_id': 75502,
}

video_insight_a = {
    'created_at': datetime.now(),
    'id': 334011,
    'video_id': 33401,
    'video_likes': 310960,
    'video_views': 856000,
}
video_insight_b = {
    'created_at': datetime.now(),
    'id': 333181,
    'video_id': 33318,
    'video_likes': 553289,
    'video_views': 1523680,
}

if __name__ == '__main__':
    create_tables()

    app.run(host='0.0.0.0', port=8000, debug=False)
