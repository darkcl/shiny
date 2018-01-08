from setuptools import setup

setup(
    name="shiny",
    version='0.2',
    py_modules=['shiny'],
    install_requires=[
        'Click',
        'terminaltables',
        'flask'
    ],
    entry_points='''
        [console_scripts]
        shiny=shiny:cli
    ''',
)
