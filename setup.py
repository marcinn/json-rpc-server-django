from setuptools import setup, find_packages

setup(
    name='damn-simple-jsonrpc-server-django',
    version='1.0',
    description='Django adapter for damn simple JSON-RPC Server',
    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author='Marcin Nowak',
    author_email='marcin.j.nowak@gmail.com',
    url='https://github.com/marcinn/json-rpc-server-django',
    keywords='web json rpc python server django',
    packages=find_packages('.'),
    install_requires=['damn-simple-jsonrpc-server>=0.4.4'],
    package_data={
        'jsonrpcdjango': ['templates/*/*'],
    },
    zip_safe=False,
)
