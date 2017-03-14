from setuptools import setup

dependency_links = []

requirements = [
    'appdirs==1.4.2',
    'packaging==16.8',
    'six==1.10.0',

    'Django==1.10.5',
    'Scrapy==1.3.0',
    'Twisted==16.6.0',

    'redis==2.10.5',
    'django-redis==4.7.0',

    'pyquery==1.2.17',
    'requests==2.12.4',

    'mysqlclient==1.3.9',

    'service-identity==16.0.0',
    'dateparser==0.5.1',
    'colorlog==2.10.0',
    'eventlet==0.20.1',
    'tldextract==2.0.2',
    'feedparser==5.2.1',

    #  'gunicorn==19.6.0',
    'ipython==5.1.0',

    'plan==0.5',

    'raven==6.0.0',
]

tests_require = [
    #  'pytest-django==3.0.0',
    #  'pyflakes==1.1.0',
    #  'pep8==1.7.0',
    #  'pytest==3.0.3',
    #  'pytest-flake8==0.7',
    #  'pytest-pep8==1.0.6',
    #  'pytest-mock==1.2',
]

circle_require = [
    #  'coverage==4.2',
]

extras_require = {
    'dev': [
        'django-debug-toolbar==1.6'
    ] + tests_require,
    'test': tests_require,
    'circle': circle_require + tests_require,
}


def main():
    setup(
        name="dronepy",
        version='0.0.1',
        install_requires=requirements,
        extras_require=extras_require,
        dependency_links=dependency_links,
        packages=[],
        package_dir={},
    )


if __name__ == "__main__":
    main()
