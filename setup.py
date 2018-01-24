from setuptools import setup

def readme():
    with open("README.rst") as f:
        return f.read()

setup(
    name = "jakopicevca",
    version = "1.0",
    description = "Program for Astro Pi 2017/18 - Mission Space Lab - Team Jakopičevca",
    long_description = readme(),
    license = "GPLv3+",
    
    packages = ["jakopicevca"],
    
    entry_points = {
        "console_scripts": ["jakopicevca=jakopicevca.__main__"],
    },
    
    install_requires = [
        "ephem"
    ],
    
    author = "Team Jakopičevca",
    author_email = "filip.stamcar@hotmail.com",
    url = "https://github.com/filips123/jakopicevca/",
    keywords = "Raspberry Pi, Astro Pi, Mission Space Lab, OŠ Riharda Jakopiča, ESA",
    platforms = "Linux",
    
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    
    include_package_data = True
)