#!/usr/bin/env python
# coding=utf-8
from PIL import Image
import sys, os, re, json, pickle

SIZE = (32, 32)
TRANSINTTOALPHA = (
  None,'0','1','2','3','4','5','6','7','8','9',
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def resizeImage(img):
  """
    img{PIL.Image}: 圖片
    size{tuple}: (長, 寬)
    
    return{PIL.Image}: 回傳 SIZE 的圖片
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

def coverImageToArray(img_file_name):
  """
    img_file_name{str}

    return value{int}
  """
  img = Image.open(img_file_name)
  pixels = img.load()
  width, height = img.size
  vector = []
  for x in range(width):
    for y in range(height):
      color = int((pixels[x,y][0] + pixels[x,y][1] + pixels[x,y][2])/3)
      vector.append(color)
  return vector

def coverImageDirToJSON(input_dir, output_file):
  out_dict = {}
  dirList = (d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d)))
  for d in dirList:
    sampleDir = os.path.join(input_dir, d)
    files = (f for f in os.listdir(sampleDir) if os.path.isfile(os.path.join(sampleDir,f)))
    for f in files:
      file_path = os.path.join(sampleDir, f)
      result = re.search('img(\d+)-(\d+).png', f)
      character = TRANSINTTOALPHA[int(result.group(1))]
      number = int(result.group(2))
      if not character in out_dict:
        out_dict[character] = {}
      out_dict[character][number] = coverImageToArray(file_path)
  with open(output_file, 'w') as f:
    f.write(json.dumps(out_dict))

def legoJson2Pickle(input_json = 'output/alldata.json', out_pickle_file = 'output/alphdatal.pkl'):
  with open(input_json) as data_file:    
    data = json.load(data_file)
  alphdata = dict()
  
  for ii in data:
    tmpl = []
    for jj in data[ii]:
      tmpl.append(data[ii][jj])
    alphdata[ii] = tmpl
  
  outfile = open(out_pickle_file, 'wb')
  pickle.dump(alphdata, outfile)
  outfile.close()