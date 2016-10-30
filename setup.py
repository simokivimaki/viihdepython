#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'viihdepython',
        version = '1.0.dev0',
        description = '''''',
        long_description = '''''',
        author = "",
        author_email = "",
        license = '',
        url = '',
        scripts = [
            'scripts/move_simpsonit',
            'scripts/delete_duplicates'
        ],
        packages = ['viihdepython'],
        py_modules = [],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe=True,
        cmdclass={'install': install},
    )
