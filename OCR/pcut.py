#!/usr/bin/python2.7  
# -*- coding: utf-8 -*- 
from PIL import Image, ImageEnhance

def cutImg(imgsrc, out_img_name, coordinate):
    """
        根据坐标位置剪切图片
    :param imgsrc: 原始图片路径(str)
    :param out_img_name: 剪切输出图片路径(str)
    :param coordinate: 原始图片上的坐标(tuple) egg:(x, y, w, h) ---> x,y为矩形左上角坐标, w,h为右下角坐标
    :return:
    """
    image = Image.open(imgsrc)
    region = image.crop(coordinate)
    region = ImageEnhance.Contrast(region).enhance(1.5)
    region.save(out_img_name)