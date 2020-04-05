#!/usr/bin/env python2.7.3

__author__ = 'simba'

# coding=utf-8

import tempfile
import shutil
from image_char import ImageChar
import random
from config import authcode_font  # 请确保改字体存在
from app_store.settings import SITE_ROOT
import os


class VerifycationCode(object):
    def destroy(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def generate(self):
        self.tmpdir = tempfile.mkdtemp()
        self.path = self.tmpdir + "/code.jpg"

        fontColor = (random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))
        size = (100, 40)
        fontPath = os.path.join(SITE_ROOT, authcode_font)
        bgColor = (255, 255, 255)
        fontSize = 20
        charNum = 4
        ic = ImageChar(fontColor, size, fontPath, bgColor, fontSize, charNum)
        self.image_str = ic.RandomString()
        ic.save(self.path)

        return self.image_str, self.path

