import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGELOG.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_mako',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    'simplejson',
    'oauth2',
    'osm_diff_tool',
    'osm_hall_monitor',
    ]

setup(name='osmhm_site',
      version='0.51',
      description='osmhm_site',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='osmhm',
      install_requires=requires,
      dependency_links = ['http://github.com/ethan-nelson/osm_hall_monitor/tarball/master#egg=osm_hall_monitor'],
      entry_points="""\
      [paste.app_factory]
      main = osmhm_site:main
      [console_scripts]
      initialize_osmhm_db = osmhm_site.scripts.initializedb:main
      """,
      )
