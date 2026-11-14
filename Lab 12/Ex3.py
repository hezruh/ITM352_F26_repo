import requests
from flask import Flask, render_template

app = Flask(__name__)

MEME_API_URL = "https://meme-api.com/gimme/wholesomememes"


def get_meme():
    response = requests.request("GET", MEME_API_URL, timeout=10)
    response.raise_for_status()
    meme = response.json()

    if not meme.get("url") or not meme.get("subreddit"):
        raise ValueError("The meme API returned incomplete meme data.")

    return meme


@app.route("/")
def memes():
    try:
        meme = get_meme()
    except (requests.RequestException, ValueError) as error:
        return render_template("memes.html", error=str(error)), 502

    return render_template(
        "memes.html",
        meme_url=meme["url"],
        subreddit=meme["subreddit"],
        error=None,
    )


@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
