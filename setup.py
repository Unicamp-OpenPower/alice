from setuptools import setup, find_packages

setup(name='alice',
      version='0.3',
      description='CLI user and project manager for Openstack',
      url='https://github.com/Unicamp-OpenPower/alice',
      author='Juliana R, Rafael Pimenta',
      author_email='juliana.orod@gmail.com, rafaelgpimenta@gmail.com',
      license='GPLv3',
      packages=find_packages(),
      install_requires=[
          'xkcdpass',
          'pathlib',
          'python-neutronclient',
          'keystoneauth1',
          'python-keystoneclient',
          'colorama',
          'python-novaclient',
          'prettytable',
          'dataset',
          'click',
          'psycopg2',
          'timestring-pleasantone'
      ],
      scripts=['bin/alice'],
      zip_safe=False)
