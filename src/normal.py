#!/usr/bin/env python
# coding=utf-8
from PIL import Image
import sys, os

SIZE = (32, 32)

def resizeImage(img):
  """
    img{PIL.Image}: 圖片
    size{tuple}: (長, 寬)
    
    return{PIL.Image}: 回傳 64x64 的圖片
  """

  return img.resize(SIZE, Image.ANTIALIAS)

def resizeImageFile(input_file_name, output_file_name):
  """
    input_file_name{str}: 輸入圖檔名稱
    output_file_name{str}: 輸出圖檔名稱

    return: None
  """
  try:
    img = Image.open(input_file_name)
  except FileNotFoundError as e:
    print(e)
    print('請輸入存在的圖片名稱')
    sys.exit(1)
  except OSError as e:
    print(e)
    print('請輸入圖片檔')
    sys.exit(1)
  img = resizeImage(img)
  img.save(output_file_name)
  return 

def resizeImageCollectioneDir(input_dir, output_dir):
  folder = input_dir.split('/')[-1] if input_dir.split('/')[-1] is not '' else input_dir.split('/')[-2]
  output_root_folder = os.path.join(output_dir, folder)
  if not os.path.exists(output_root_folder):
    os.mkdir(output_root_folder)
  dirList = (d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d)))
  for d in dirList:
    in_dir = os.path.join(input_dir, d)
    out_dir = os.path.join(output_root_folder, d)
    if not os.path.exists(out_dir):
      os.mkdir(out_dir)
    resizeImageDir(in_dir, out_dir)
def resizeImageDir(input_dir, output_dir):
  files = (f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)))
  for f in files:
    input_path = os.path.join(input_dir, f)
    output_path = os.path.join(output_dir, f)
    resizeImageFile(input_path, output_path)

def coverImageToArray(img):
  pass
