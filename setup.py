from distutils.core import setup

setup(
    name='WorlRealTimeCurrency',
    version='1.0',
    author='Eduardo Erlo',
    author_email='eduardo.erlo@gmail.com',
    packages=['wrtc',],
    scripts=[],
    url='',
    license='LICENSE',
    description='Python class to get real-time currency values, based on the information providing backends.',
    long_description=open('README.md').read(),
    install_requires=[
        "cssselect==0.9.1",
        "lxml==3.3.5"
    ],
)