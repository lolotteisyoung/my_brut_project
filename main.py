import os
import requests
from datetime import datetime


page = {
    "created_at": str(datetime.now()),
    "id": 70515,
    "name": "Our Media France"
}

video_a = {
    "created_at": str(datetime.now()),
    "id": 33401,
    "title": "Parlons Cash",
    "page_id": 70501,
}
video_b = {
    "created_at": str(datetime.now()),
    "id": 33318,
    "title": "Privés d'écran",
    "page_id": 75502,
}

video_insight_a = {
    "created_at": str(datetime.now()),
    "id": 33401,
    "video_id": 1,
    "likes": 310960,
    "views": 856000,
}
video_insight_b = {
    "created_at": str(datetime.now()),
    "id": 33318,
    "video_id": 2,
    "likes": 553289,
    "views": 1523680,
}


def main():
    #Create New Pages
    try:
        requests.post("http://localhost:8000/page/add", json=page)
    except:
        print("the page was not added to the database")

    #Create Video A
    vida = requests.post("http://localhost:8000/video/add", json=video_a)
    try:
        requests.post("http://localhost:8000/video/add", json=video_a)
        print(vida.text)
    except:
        print(vida.text)
        print("the video A was not added to the database")

    #Create Video B
    try:
        requests.post("http://localhost:8000/video/add", json=video_b)
    except:
        print("the video B was not added to the database")

    #Create Video A"s insight
    try:
        requests.post("http://localhost:8000/insight/add", json=video_insight_a)
    except:
        print("the video B was not added to the database")
    #Create Video B"s insight
    try:
        requests.post("http://localhost:8000/insight/add", json=video_insight_b)
    except:
        print("the video B was not added to the database")

    #Delete Video B
    try:
        requests.delete(f"http://localhost:8000/video/{video_b['id']}")
    except:
        print("the video B was not deleted")

if __name__=="__main__":
    main()

