from setuptools import setup, find_packages

if __name__ == '__main__':
    package_name = 'slave'

    setup(
        name=package_name,
        author='Mr Foo',
        version='0.0.1',
        packages=find_packages(),
        install_requires=['fabric'],
        package_dir={package_name: package_name}
    )
