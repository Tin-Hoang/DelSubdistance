'''
-------
License
-------

It is released under the MIT license.

    Copyright (c) 2013 Hiroyuki Tanaka

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


try:
    from setuptools import setup, Extension
except:
    from distutils import setup, Extension
# for development
# from Cython.Build import cythonize
# ext_modules = cythonize('DelSubdistance/bycython.pyx')

ext_modules = [
    Extension(
        'DelSubdistance.bycython',
        ['DelSubdistance/_DelSubdistance.cpp', 'DelSubdistance/bycython.cpp'],
        include_dirs=['./DelSubdistance'],
    )
]

setup(
    name="DelSubdistance",
    version='1.0.0',
    description="Fast implementation of the Levenshtein distance with only Deletion and Substitution errors",
    long_description='',
    url='https://www.github.com/Tin-Hoang/DelSubdistance',
    ext_modules=ext_modules,
    packages=['DelSubdistance'],
    package_data={'DelSubdistance': ['_DelSubdistance.h', 'def.h']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
