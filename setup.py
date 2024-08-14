from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pycellga',  
    version='0.1.0',  
    description='A Python Package for Improved Cellular Genetic Algorithms',  
    author='SEVGİ AKTEN KARAKAYA, MEHMET HAKAN SATMAN',  
    author_email='sevgiakten@gmail.com, mhsatman@gmail.com',  
    packages=find_packages(),  
    install_requires=required, 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
