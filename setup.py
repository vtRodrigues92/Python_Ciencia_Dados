# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

package_data = \
{'': ['*']}

packages = \
['vtr_csv_json_converter']

entry_points = \
{'console_scripts': ['csv_converter = '
                     'vtr_csv_json_converter.converter:converter']}


 
setup(name='vtr_csv_json_converter',
      version='0.2.0',
      license='MIT',
      author='Victor de Oliveira Rodrigues',
      author_email='victor.o.rodrigues11@gmail.com',
      description='Conversor csv para json. Publicação apenas para fins de aprendizagem na PUC. Classe DS.',
      packages=packages,
      package_data = package_data,
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires = \
            ['click>=8.0.1,<9.0.0'],
      entry_points = entry_points)
      
      


