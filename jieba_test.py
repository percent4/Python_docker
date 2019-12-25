# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2:09 下午
import os, re, json, traceback
import jieba

if __name__ == '__main__':
    sent = '最近这几天，我都在三亚上班，看着海开发的感觉还不错。'
    print(list(jieba.cut(sent)))