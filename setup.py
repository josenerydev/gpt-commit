from setuptools import setup, find_packages

setup(
    name='gpt-commit',
    version='0.1.1',
    description="A command-line tool that intelligently generates commit messages based on staged file changes in Git using OpenAI's GPT.",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/josenerydev/gpt-commit',
    author='José Nery',
    author_email='josenerydev@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
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
