from setuptools import setup, find_packages


readme = open('README.md').read()

setup(name="packagesimple",
      version='0.0.1',
      packages=find_packages(),
      description="Simple python package example",
      long_description=readme,
      author="Sam Lea",
      author_email="samjlea@gmail.com",
      url="",
      install_requires=[],
      scripts=[],
      entry_points={},
      )
