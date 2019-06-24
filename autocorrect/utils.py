# Python 3 Spelling Corrector
#
# Copyright 2014 Jonas McCallum.
# Updated for Python 3, based on Peter Norvig's
# 2007 version: http://norvig.com/spell-correct.html
#
# Open source, MIT license
# http://www.opensource.org/licenses/mit-license.php
"""
File reader, concat function and dict wrapper

Author: Jonas McCallum
https://github.com/foobarmus/autocorrect

"""
import os
import re
import zipfile
from contextlib import closing

PATH = os.path.abspath(os.path.dirname(__file__))
RE = '[A-Za-z]+'
ZIP = 'words.zip'
ZIP_FOLDER = 'words'

def words_from_archive(filename, include_dups=False, map_case=False):
    """extract words from a text file in the archive"""
    zip_path = os.path.join(PATH, ZIP)
    with closing(zipfile.ZipFile(zip_path)) as t:
        with closing(t.open(f'{ZIP_FOLDER}/{filename}')) as f:
            words = re.findall(RE, f.read().decode(encoding='utf-8'))
    if include_dups:
        return words
    elif map_case:
        return {w.lower():w for w in words}
    else:
        return set(words)
