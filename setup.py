from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="django_transitive_dag",
    version="0.1",
    description="SQL Directed Acyclic Graph models for Django",
    long_description=readme(),
    url="https://github.com/Maxbot100/django-transitive-dag",
    author="Max Mattes",
    author_email="maxbot1539@gmail.com",
    license="GPLV3+",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'Django>=1.11'
    ],
    python_requires=">=3.4",
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Topic :: Utilities',
    ]
)
