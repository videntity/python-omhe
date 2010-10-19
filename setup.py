from setuptools import setup, find_packages

setup(name="python-omhe",
      version="0.3",
      description="OMHE: Open Mobile Health Exchange Parser",
      long_description="""\
Open Mobile Health Exchange Parser provides libraries to parse OMHE strings.
Sample code to connect a Wii Balance Board, blood pressure meters, and more. 
""",
      author="Alan Viars",
      author_email="aviars@videntity.com",
      url="http://gitbub.com/aviars/python-omhe",
      download_url="http://github.com/aviars/python-omhe/tarball/master",
      packages=find_packages(exclude='tests'),
      package_data={'omhe': ['omhe/hardware/wiibalance/*.ini']},
      #install_requires=['Paper>=1.0', 'UPSCode'],
      scripts=['omhe/bin/parseomhe',
               'omhe/bin/restcat-login-test.py',
               'omhe/bin/upload2restcat',
               'omhe/hardware/bloodpressure_a_and_d_UA767PC/bloodpressure.py',
               'omhe/hardware/wiibalance/scalesgui.py',
               'omhe/hardware/wiibalance/weight.py',
               'omhe/hardware/wiibalance/wiibal-weighdemo.py',
               ]
      )
