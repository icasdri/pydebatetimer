from setuptools import setup, find_packages

setup(
    name='pybatterymonitor',
    version='0.1',
    license='GPL3',
    author='icasdri',
    author_email='icasdri@gmail.com',
    description='A small GTK application for public forum debate timing',
    url='https://github.com/icasdri/pydebatetimer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    entry_points={
        'gui_scripts': ['pydebatetimer = pydebatetimer.main:main'],
    }
)
