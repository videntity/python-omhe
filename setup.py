from setuptools import setup, find_packages

setup(name="python-omhe",
      version="0.2dev",
      description="Open Mobile Health Exchange Parser",
      long_description="""\
Open Mobile Health Exchange Parser provides libraries to parse OMHE strings.
Lots more to come!
""",
      author="Alan Viars",
      author_email="aviars@videntity.com",
      url="http://code.google.com/p/omhe",
      download_url="http://omhe.google.com/files/python-omhe-02dev.tar.gz",
      packages=find_packages(exclude='tests'),
      package_data={'omhe': ['data/*.json']},
      #install_requires=['Paper>=1.0', 'UPSCode'],
      )
