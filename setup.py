from setuptools import setup
setup(
    name = 'henzcli',
    version = '0.1.0',
    packages = ['henzcli'],
    tests_require=['pytest', 'coverage'],
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
            'henzcli = main:main'
        ]
    })
