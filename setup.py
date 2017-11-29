from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='jakopicevca',
      version='1.0',
      description='Program for Astro Pi 2017/18 - Mission Space Lab, team Jakopičevca.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: Unix',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Astronomy',
      ],
      keywords='Astro Pi, Mission Space Lab, OŠ Riharda Jakopiča',
      url='http://github.com/filips123/jakopicevca',
      author='Team Jakopičevca',
      author_email='filip.stamcar@hotmail.com',
      license='GPLv3+',
      packages=['jakopicevca'],
      platforms='Linux',
      install_requires=[
          'sense-hat',
          'picamera',
          'ephem'
      ],
      python_requires='>=3',
      include_package_data=True)