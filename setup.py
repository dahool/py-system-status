from setuptools import setup

setup(
    name='PyStatus',
    version='0.1-dev',
    url='',
    license='GPLv3+',
    author='Sergio Gabriel Teves',
    author_email='',
    description='Python System Status',
    long_description=__doc__,
    packages=['pystatus'],
    include_package_data=True,
    zip_safe=False,
    platforms='linux',
    install_requires=[
        'flask-peewee>=0.5.6',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
