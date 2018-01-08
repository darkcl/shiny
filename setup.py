from setuptools import setup, find_packages

setup(
    name="shiny",
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
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
