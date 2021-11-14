#!/bin/env python
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Ahmed Gharib
# DATE CREATED: Sun Nov 14 2021
# REVISED DATE: Sun Nov 14 2021
# PURPOSE: MemeEngine class to generate image with meme text
#
##

import pathlib
from random import randint
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Class method for MemeEngine ."""

    def __init__(self, output_dir_path: str) -> None:
        """Initialize the MemEngine class .

        Args:
            output_dir_path (str): path to the output directory.
        """
        self.output_dir_path = pathlib.Path(output_dir_path)
        if not self.output_dir_path.exists():
            self.output_dir_path.mkdir()

        self.counter_dict = {}

    def make_meme(
        self,
        image_path: str,
        quote_body: str,
        quote_author: str,
        img_width: int = 500,
    ) -> str:
        """Draw meme on top of the image and save it in the output directory.

        Args:
            image_path (str): path to the image.
            quote_body (str): quote body.
            quote_author (str): quote author
            img_width (int, optional): image width. Defaults to 500.

        Returns:
            str: path to the new image.
        """
        img = Image.open(image_path)

        if img_width is not None:
            ratio = img_width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((img_width, height), Image.NEAREST)

        draw = ImageDraw.Draw(img)
        font_body = ImageFont.truetype("./fonts/RoadRage-Regular.ttf", size=30)
        font_auther = ImageFont.truetype(
            "./fonts/RoadRage-Regular.ttf", size=20
        )
        qoute_positions = (30, randint(30, height - 40))
        draw.text(
            qoute_positions,
            quote_body,
            font=font_body,
            fill="#000",
            stroke_width=1,
            stroke_fill="#fff",
        )
        author_positions = (40, qoute_positions[1] + 30)
        draw.text(
            author_positions,
            f"- {quote_author}",
            font=font_auther,
            fill="#000",
            stroke_width=1,
            stroke_fill="#fff",
        )

        fpath_part = f"{quote_author}-{quote_body}"
        count = self.counter_dict.get(fpath_part, 0)
        out_path = self.output_dir_path / (fpath_part + str(count) + ".png")
        self.counter_dict[fpath_part] = count + 1

        img.save(out_path)
        return out_path
