from setuptools import setup, find_packages

setup(name='damn-simple-jsonrpc-server-django',
      version='0.2.2',
      description='Django adapter for damn simple JSON-RPC Server',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      author='Marcin Nowak',
      author_email='marcin.j.nowak@gmail.com',
      url='https://github.com/marcinn/json-rpc-server-django',
      keywords='web json rpc python server django',
      packages=find_packages('.'),
      install_requires=['damn-simple-jsonrpc-server>=0.3'],
      package_data={
          'jsonrpcdjango': ['templates/*/*'],
          },
      zip_safe=False,
      )

