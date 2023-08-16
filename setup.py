from setuptools import setup, find_packages

setup(
    name="gpt_commit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai',
        # qualquer outra dependência que seu projeto necessite
    ],
    entry_points={
        'console_scripts': [
            'gpt-commit = gpt_commit.gpt_commit:main',
        ],
    },
)
