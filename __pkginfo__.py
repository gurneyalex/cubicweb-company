# pylint: disable-msg=W0622
"""cubicweb-company application packaging information"""

distname = 'cubicweb-company'

numversion = (0, 2, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
copyright = '''Copyright (c) 2008 LOGILAB S.A. (Paris, FRANCE).
http://www.logilab.fr/ -- mailto:contact@logilab.fr'''

author = 'Logilab'
author_email = 'contact@logilab.fr'

short_desc = 'companies and divisions'
long_desc = '''companies and divisions'''

from os import listdir as _listdir
from os.path import join, isdir

from glob import glob
scripts = glob(join('bin', 'company-*'))

web, ftp = '', ''

pyversions = ['2.4']

#from cubicweb.devtools.pkginfo import get_distutils_datafiles
CUBES_DIR = join('share', 'cubicweb', 'cubes')
THIS_CUBE_DIR = join(CUBES_DIR, 'company')

def listdir(dirpath):
    return [join(dirpath, fname) for fname in _listdir(dirpath)
            if fname[0] != '.' and not fname.endswith('.pyc')
            and not fname.endswith('~')]

try:
    data_files = [
        # common files
        [THIS_CUBE_DIR, [fname for fname in glob('*.py') if fname != 'setup.py']],
     
        # client (web) files
        [join(THIS_CUBE_DIR, 'data'),  listdir('data')],
        [join(THIS_CUBE_DIR, 'i18n'),  listdir('i18n')],
        [join(THIS_CUBE_DIR, 'views'), listdir('views')],
        # Note: here, you'll need to add views' subdirectories if you want
        # them to be included in the debian package
        
        # server files
        [join(THIS_CUBE_DIR, 'migration'), listdir('migration')],
        ]
except OSError:
    # we are in an installed directory
    pass

__use__ = ('addressbook',)

cube_eid = None # <=== FIXME if you need direct bug-subscription

