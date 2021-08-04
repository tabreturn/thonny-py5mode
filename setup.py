import pathlib
from setuptools import setup

README = (pathlib.Path(__file__).parent / 'README.md').read_text()

setup(
  name='thonny-py5mode',
  version='0.1.0-alpha',    
  description='py5 mode plugin for Thonny',
  long_description = README,
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
  #install_requires=['install-jdk', 'py5']  # uncomment when the new py5 is released
  install_requires=['install-jdk'], dependency_links=['https://github.com/hx2A/py5.git@0.5a1.dev0#egg=py5']  # comment when the new py5 is released
)
