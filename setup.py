import setuptools


setuptools.setup(
    name='pytest-fixtures',
    version='0.0.4',

    author='Max Zheng',
    author_email='maxzheng.os@gmail.com',

    description='Common fixtures for pytest',
    long_description=open('README.rst').read(),

    url='https://github.com/maxzheng/pytest-fixtures',

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    python_requires='>=3.6',
    setup_requires=['setuptools-git'],

    entry_points={
       'pytest11': [
           'standard = fixtures',
           'click = fixtures.click',
       ],
    },

    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Testing :: Unit',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='common pytest fixtures',
)
