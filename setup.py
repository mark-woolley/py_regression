from setuptools import setup

setup(name='py_regression',
      version=0.1,
      description='toy regression package',
      author='mark.woolley',
      packages=['py_regression'],
      install_requires=['statsmodels',
                        'unittest2',
                        'pandas'],
      test_suite='nose.collector',
      tests_require=['nose']
      )