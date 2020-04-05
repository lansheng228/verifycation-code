#!/usr/bin/env python2.7.3

__author__ = 'simba'

# coding=utf-8

from PIL import Image, ImageDraw, ImageFont
import random
from random_chinese_character import RandomChineseCharacter
from random_letter_number import RandomLetterNumber


class ImageChar(object):
    def __init__(self, fontColor, size, fontPath, bgColor, fontSize, charNum):
        self.size = size
        self.fontPath = fontPath
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = ImageFont.truetype(self.fontPath, self.fontSize)
        self.image = Image.new('RGB', size, bgColor)
        self.charNum = charNum

    def __rotate(self):
        self.image.rotate(random.randint(0, 360), expand=0)

    def __drawText(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)
        del draw

    def __randRGB(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def __randPoint(self):
        (width, height) = self.size
        return (random.randint(0, width), random.randint(0, height))

    def __randLine(self, max_num):
        draw = ImageDraw.Draw(self.image)
        num = random.randint(1, max_num)
        for i in range(0, num):
            draw.line([self.__randPoint(), self.__randPoint()], self.__randRGB())
        del draw

    def RandomString(self):
        gap = 5
        start = 0
        rand_str = ""
        for i in range(0, self.charNum):
            j = random.randint(0, 1)
            if j == 0:
                char = RandomChineseCharacter.Unicode()
            else:
                char = RandomLetterNumber.LetterNumber()
            rand_str = rand_str + char
            x = start + self.fontSize * i + random.randint(0, gap) + gap * i
            self.__drawText((x, random.randint(-5, 5)), char, self.__randRGB())
            self.__rotate()
        self.__randLine(10)

        return rand_str

    def save(self, path):
        self.image.save(path)
