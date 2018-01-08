from setuptools import setup

setup(
    name="shiny",
    version='0.2',
    py_modules=['cli', 'core', 'web'],
    install_requires=[
        'Click',
        'terminaltables',
        'flask'
    ],
    entry_points='''
        [console_scripts]
        shiny=cli:cli
    ''',
)
