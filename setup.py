import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-telegram-login',
    version='0.0.1',
    packages = find_packages(
        exclude=[
            'login_app*',
            'django_telegram_tools',
        ]
    ),
    include_package_data=True,
    license='MIT',
    description='The reusable Django application for Telegram authorization.',
    url='https://github.com/dadoxr/django-telegram-login',
    author='Roman Uglov',
    author_email='uglovrv@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
