import os
import shutil
import zipfile
import re

dirs = [
    'resources',
    'resources/language',
    'resources/language/English'
]
files = [
    'addon.xml',
    'addon.py',
    'swefilm.py',
    'parsers.py',
    'utils.py',
    'resources/language/English/strings.xml'
]

with open("addon.xml") as f:
    version_re = re.search(r'<addon.*version="(.*?)"', f.read())
    version = version_re.group(1)

    dirname = "plugin.video.swefilm"
    zipname = "plugin.video.swefilm-%s.zip" % version
    os.mkdir(dirname)

    for dir in dirs:
        os.mkdir(os.path.join(dirname, dir))

    for file in files:
        shutil.copyfile(file, os.path.join(dirname, file))

    with zipfile.ZipFile(zipname, 'w') as z:
        for root, dirs, files in os.walk(dirname):
            for file in files:
                z.write(os.path.join(root, file))
