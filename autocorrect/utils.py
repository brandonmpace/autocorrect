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
import re, os, tarfile
from contextlib import closing

PATH = os.path.abspath(os.path.dirname(__file__))
BZ2 = 'words.tar.bz2'
RE = '[A-Za-z]+'

def words_from_archive(filename, include_dups=False, map_case=False):
    """extract words from a text file in the archive"""
    bz2 = os.path.join(PATH, BZ2)
    tar_path = '{}/{}'.format('words', filename)
    with closing(tarfile.open(bz2, 'r:bz2')) as t:
        with closing(t.extractfile(tar_path)) as f:
            words = re.findall(RE, f.read().decode(encoding='utf-8'))
    if include_dups:
        return words
    elif map_case:
        return {w.lower():w for w in words}
    else:
        return set(words)
