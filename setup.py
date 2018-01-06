from setuptools import setup

setup(
    name="shiny",
    version='0.1',
    py_modules=['shiny'],
    include_package_data=True,
    packages=['cli'],
    install_requires=[
        'Click',
        'terminaltables',
        'Flask'
    ],
    entry_points='''
        [console_scripts]
        shiny=cli:cli
    ''',
)
