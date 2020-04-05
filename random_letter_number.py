#!/usr/bin/env python2.7.3

__author__ = 'simba'

# coding=utf-8

import random
import string


class RandomLetterNumber(object):
    """
    用于随机生成数字和字母
    """

    @staticmethod
    def LetterNumber():
        allw = string.ascii_letters + string.digits
        letter_number = random.choice(allw)

        return letter_number
