from setuptools import setup
setup(
    name = 'henzcli',
    version = '0.1.0',
    packages = ['henzcli'],
    install_requires = [
        'requests',
        'beautifulsoup4',
        'python-dotenv',
        'colorama',
        'black',
        'flake8'
    ],
    entry_points = {
        'console_scripts': [
            'henzcli = henzcli.__main__:main'
        ]
    })
