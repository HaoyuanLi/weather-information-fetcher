from distutils.core import setup
import py2exe

setup(console=['weatherFetcher.py'],
      options={
          'py2exe': {
              'packages': ['beautifulsoup','requests']
          }
      }
)