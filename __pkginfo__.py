# pylint: disable-msg=W0622
"""cubicweb-company application packaging information"""

modname = 'company'
distname = 'cubicweb-%s' % modname

numversion = (0, 5, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'

author = 'Logilab'
author_email = 'contact@logilab.fr'
web = 'http://www.cubicweb.org/project/%s' % distname
description = 'company component for the CubicWeb framework'

classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    ]

__depends__ = {'cubicweb': '>= 3.9.0',
               'cubicweb-addressbook': None}

# packaging ###

from os import listdir as _listdir
from os.path import join, isdir
from glob import glob

CUBES_DIR = join('share', 'cubicweb', 'cubes')
THIS_CUBE_DIR = join(CUBES_DIR, 'company')

try:
    data_files = [
        # common files
        [THIS_CUBE_DIR, [fname for fname in glob('*.py') if fname != 'setup.py']],
        ]
    # check for possible extended cube layout
    for dirname in ('entities', 'views', 'sobjects', 'hooks', 'schema', 'data', 'i18n', 'migration'):
        if isdir(dirname):
            data_files.append([join(THIS_CUBE_DIR, dirname), listdir(dirname)])
    # Note: here, you'll need to add subdirectories if you want
    # them to be included in the debian package
except OSError:
    # we are in an installed directory
    pass
