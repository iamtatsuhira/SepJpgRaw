import sys
import os
import shutil

JPG_EXTENSIONS = set(['jpg', 'JPG'])
RAW_EXTENSIONS = set(['ARW', 'arw'])
MTS_EXTENSIONS = set(['MTS', 'mts'])
MP4_EXTENSIONS = set(['mp4', 'MP4'])

JPG_DIRNAME = 'jpg'
RAW_DIRNAME = 'raw'
MTS_DIRNAME = 'MTS'
MP4_DIRNAME = 'mp4'

filename = sys.argv[1]
extension = filename.rsplit('.', 1)[1]

if extension in JPG_EXTENSIONS:
    # 必要であればディレクトリの作成
    if not os.path.isdir(JPG_DIRNAME):
        os.mkdir(JPG_DIRNAME)
    shutil.move(filename, JPG_DIRNAME)
if extension in RAW_EXTENSIONS:
    # 必要であればディレクトリの作成
    if not os.path.isdir(RAW_DIRNAME):
        os.mkdir(RAW_DIRNAME)
    shutil.move(filename, RAW_DIRNAME)
if extension in MTS_EXTENSIONS:
    # 必要であればディレクトリの作成
    if not os.path.isdir(MTS_DIRNAME):
        os.mkdir(MTS_DIRNAME)
    shutil.move(filename, MTS_DIRNAME)
if extension in MP4_EXTENSIONS:
    # 必要であればディレクトリの作成
    if not os.path.isdir(MP4_DIRNAME):
        os.mkdir(MP4_DIRNAME)
    shutil.move(filename, MP4_DIRNAME)



