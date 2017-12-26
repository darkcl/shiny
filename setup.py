from setuptools import setup

setup(
    name="shiny",
    version='0.1',
    py_modules=['shiny'],
    install_requires=[
        'Click',
        'terminaltables'
    ],
    entry_points='''
        [console_scripts]
        shiny=shiny:cli
    ''',
)
