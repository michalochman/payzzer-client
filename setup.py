# https://pythonhosted.org/an_example_pypi_project/setuptools.html
# http://www.siafoo.net/article/77

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='payzzer_client',
    version='2.0',
    packages=['payzzer_client', 'tests'],
    url='https://github.com/michalochman/payzzer-client',
    license='MIT',
    keywords='payzzer api client',
    author='Michal Ochman',
    author_email='michoch@gmail.com',
    description='Client for Payzzer API v2',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    install_requires=[
        'requests',
        'pyOpenSSL',
        'ndg-httpsclient',
        'pyasn1',
    ]
)
