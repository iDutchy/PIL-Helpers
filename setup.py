from distutils.core import setup

setup(
  name = 'pil_helper',
  packages = ['pil_helper'],
  version = '0.0.1',
  license='MIT',
  description = 'A couple helper methods for working with PIL',
  author = 'Niels Steenman',
  author_email = 'ngssteenman@gmail.com',
  url = 'https://github.com/iDutchy/PIL-Helpers',
  keywords = ['PIL', 'pillow'],
  install_requires=['pillow'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)