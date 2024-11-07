from setuptools import setup,find_packages

setup(
  name='rcapi',
  author='rc-csmith',
  packages = find_packages(),
  description='Red Canary API SDK',
  version='0.1',
  install_requires =['requests','pyjson']
)