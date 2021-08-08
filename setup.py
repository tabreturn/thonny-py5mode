import pathlib
from setuptools import setup

README = (pathlib.Path(__file__).parent / 'README.md').read_text()

setup(
  name='thonny-py5mode',
  version='0.1.14-alpha',
  description='py5 mode plugin for Thonny',
  long_description=README,
  long_description_content_type='text/markdown',
  url='https://github.com/tabreturn/thonny-py5mode',
  author='tabreturn',
  author_email='thonny-py5mode@tabreturn.com',
  license='WTFPL',
  classifiers=[
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    'Environment :: Plugins',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Text Editors :: Integrated Development Environments (IDE)'
  ],
  packages=['thonnycontrib.thonny-py5mode'],
  install_requires=['install-jdk', 'py5']
)
