from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='keypath',
  version='0.0.2',
  description='Get/set values at a key path in a dict/object',
  long_description=readme,
  author='Brian Hammond',
  author_email='brian@fictorial.com',
  url='https://github.com/fictorial/keypath',
  license=license,
  packages=find_packages(exclude=('tests', 'docs'))
)
