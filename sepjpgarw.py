import sys
import os
import shutil

JPG_EXTENSIONS = set(['jpg', 'JPG'])
RAW_EXTENSIONS = set(['ARW', 'arw'])

JPG_DIRNAME = 'jpg'
RAW_DIRNAME = 'raw'

# 必要であればディレクトリの作成
if not os.path.isdir(JPG_DIRNAME):
    os.mkdir(JPG_DIRNAME)
if not os.path.isdir(RAW_DIRNAME):
    os.mkdir(RAW_DIRNAME)

filename = sys.argv[1]
extension = filename.rsplit('.', 1)[1]

if extension in JPG_EXTENSIONS:
    shutil.move(filename, JPG_DIRNAME)
if extension in RAW_EXTENSIONS:
    shutil.move(filename, RAW_DIRNAME)



