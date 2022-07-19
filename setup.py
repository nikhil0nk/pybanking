from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name='pybanking',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    version='0.2',
    license='MIT',
    author="Shorthills Tech",
    author_email='apurv@shorthillstech.com',
    packages=find_packages('pybanking'),
    package_dir={'': 'pybanking'},
    url='https://github.com/shorthills-tech/pybanking',
    keywords='banking project',
    install_requires=[
          'scikit-learn',
      ],

)
