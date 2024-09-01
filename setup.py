from setuptools import setup, find_packages

setup(
    name='MVCForge',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mvc-generate=MVCForge.generator:main'
        ]
    },
    description='A simple MVC project structure generator',
    author='Victor Roza Souza',
    author_email='victorroza22@gmail.com',
    url='https://github.com/Vicrrs/MVCForge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
