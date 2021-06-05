from pytube import YouTube
import time
from flask import Flask, render_template, url_for, request
from flask_cors import CORS
from hurry.filesize import size

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api/youtube')
def youtube():
    url = request.args.get('url')
    if url:
        yt = YouTube(url)
        video = {
            "info": {
                "title": yt.title,
                "author": yt.author,
                "thumbnail": yt.thumbnail_url,
                "description": yt.description,
                "length": time.strftime("%H:%M:%S", time.gmtime(yt.length)),
                "views": yt.views,
                "publish_date": yt.publish_date,
                "chanel": yt.channel_url,
                "raiting": yt.rating,
                "publish_date": yt.publish_date,
                "js_url": yt.js_url
            },
            "sources": []
        }
        videos = yt.streams.filter(progressive=True)
        for v in videos:
            video['sources'].append({
                "url": v.url,
                "size":size(v.filesize),
                "resolution": v.resolution
            })
        return video



if __name__ == '__main__':
    app.run(debug=True)