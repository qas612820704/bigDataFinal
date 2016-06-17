#!/usr/bin/env python
# coding=utf-8
from PIL import Image
import sys

def resizeImgTo64_64(img):
  """
    img{PIL.Image}: 圖片
    
    return{PIL.Image}: 回傳 64x64 的圖片
  """

  return img.resize((64, 64), Image.ANTIALIAS)

def resizeImgFileTo64_64(input_file_name, output_file_name):
  """
    input_file_name{str}: 輸入圖檔名稱
    output_file_name{str}: 輸出圖檔名稱

    return: None
  """
  try:
    img = Image.open(input_file_name)
  except FileNotFoundError as e:
    print('請輸入存在的圖片名稱')
    print(e)
    sys.exit(1)
  except OSError as e:
    print('請輸入圖片檔')
    print(e)
    sys.exit(1)
  img = resizeImgTo64_64(img)
  img.save(output_file_name)
  return 

def resizeImageDir(input_dir, out_dir):
  pass
