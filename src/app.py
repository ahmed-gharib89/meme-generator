#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sat Nov 13 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE:
#
##

import random
import os
import requests
import pathlib
from flask import Flask, render_template, abort, request
from PIL import UnidentifiedImageError

from quotes import Ingestor
from meme_engine import MemeEngine

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    # Done: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = pathlib.Path("./_data/photos/dog/")

    # Done: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = list(images_path.glob("*.jpg"))

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get("image_url")
    if not image_url:
        abort(400)

    try:
        response = requests.get(image_url)
        if response.status_code != 200:
            abort(400)
    except Exception as error:
        print(error)
        abort(400)

    temp_img = "./temp.png"
    with open(temp_img, "wb") as img:
        img.write(response.content)

    body = request.form.get("body")
    author = request.form.get("author")

    try:
        path = meme.make_meme(temp_img, body, author)
    except UnidentifiedImageError as error:
        print(error)
        abort(400)

    os.remove(temp_img)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
