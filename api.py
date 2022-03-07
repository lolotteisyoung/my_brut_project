from flask import Flask, request, jsonify
import my_operator
from datetime import datetime
from my_database import create_tables

app = Flask(__name__)


@app.route("/pages", methods=["GET"])
def get_pages():
    pages = my_operator.get_pages()
    return jsonify(pages)


@app.route("/videos", methods=["GET"])
def get_videos():
    videos = my_operator.get_videos()
    return jsonify(videos)


@app.route("/insights", methods=["GET"])
def get_insights():
    insights = my_operator.get_insights()
    return jsonify(insights)


@app.route("/insights/<id>", methods=["GET"])
def get_insights_by_video_id(id):
    insights = my_operator.get_insights_by_video(id)
    return jsonify(insights)


@app.route("/page/add", methods=["POST"])
def add_page():
    page_info = request.get_json()
    return jsonify(my_operator.create_page(page_info))


@app.route("/video/add", methods=["POST"])
def add_video():
    video_info = request.get_json()
    return jsonify(my_operator.create_video(video_info))


@app.route("/insight/add", methods=["POST"])
def add_insight():
    insight_info = request.get_json()
    return jsonify(my_operator.create_insight(insight_info))


@app.route("/page/<id>", methods=["DELETE"])
def delete_page(id):
    action = my_operator.delete_page(id)
    return jsonify(action)


@app.route("/video/<id>", methods=["DELETE"])
def delete_video(id):
    action = my_operator.delete_video(id)
    return jsonify(action)


@app.route("/insight/<id>", methods=["DELETE"])
def delete_insight(id):
    action = my_operator.delete_insight(id)
    return jsonify(action)


if __name__ == "__main__":
    create_tables()
    app.run(port=8000, debug=False)
