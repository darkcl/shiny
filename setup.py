from setuptools import setup, find_packages

setup(
    name="shiny",
    version='0.2',
    py_modules=['cli', 'core', 'web'],
    packages=find_packages(),
    include_package_data=True,
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
