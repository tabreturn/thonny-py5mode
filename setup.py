import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
  name='thonny-py5mode',
  version='0.0.1',    
  description='py5 plugin for Thonny',
  url='https://github.com/user/repo',
  author='author name',
  author_email='author@domain.ext',
  license='the licence',
  packages=['thonnycontrib.thonny-py5mode'],
  install_requires=['install-jdk'],
  dependency_links=['https://github.com/hx2A/py5.git@0.5a1.dev0#egg=py5'],
  classifiers=[
    # complete classifier list: https://pypi.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 1 - Planning'
  ]
)
