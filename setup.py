from setuptools import setup, find_packages

setup(
    name='py-crud',
    version='0.1.0',
    packages=find_packages(),
    
    install_requires=[
        'pandas',
        'python-dotenv',
    ],
    
    license='MIT', 
)