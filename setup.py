from setuptools import setup, find_packages

setup(
    name='gpt-commit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'gpt-commit=gpt_commit.gpt_commit:main',
        ],
    },
)
