from setuptools import setup


setup(name='pygulmohar',
      version='0.1',
      description='Python clients for Python implementation of [MDP/0.2](https://rfc.zeromq.org/spec/18/)',
      author='Shishir Pandey',
      author_email='shishir.py@gmail.com',
      license='MPL 2.0',
      packages=['pygulmohar'],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Mozilla Public License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )