import sys
import time
import os.path

__all__ = ('parse_version', 'version')
__version__ = '2020.2.7'


def parse_version(line):
    '''
        Type
            line:   bytes
            return: str

        Example
            >>> parse_version(b"__version__ = '2020.2.3'\n")
            '2020.2.3'
    '''
    if line:
        # remove ', ", " ", '\n'
        line = line.replace(b'"', b'').replace(b"'", b'').replace(b' ', b'').replace(b'\n', b'')
        # e.g `__version__=2020.2.3`
        _, _, version = line.partition(b'=')
        # e.g '2020.2.3' or ''
        return version.decode() if b'.' in version else ''
    else:
        return ''


def version(package, revision=''):
    ''' Lazy persons version generator using `year.month.day` as its value.

        Type
            package:    str     # package directory
            revision:   str
            return:     str

        Example
            >>> version('pacakge_name')
            '2020.2.3'

            >>> version('pacakge_name', 'v1')
            '2020.2.3v1'

        Usage
            >>> from versioning import version
            ...
            >>> setup(...,
            >>>       setup_requires=['versioning'],
            >>>       version=version('mylib'),
            >>>       ...)

        Note
            - Auto generates date as version number, sets it in `setup(version='2020.2.3')` also
            replaces `__init__.py` file `__version__` line with `__version__ = '2020.2.3'`
            - only generates version if `python3 setup.py sdist` else uses the old version.
    '''
    # Package
    init_path = os.path.join(package, '__init__.py')
    if not os.path.isfile(init_path):
        # One-Off Script
        init_path = package + '.py'
        if not os.path.isfile(init_path):
            _ = f'did not find `{package}/__init__.py` or one-off script `{package}.py` file.'
            raise FileNotFoundError(_)

    with open(init_path, 'rb+') as file:
        # "__init__.py" file content
        content = file.readlines()

        # Find `__version__ = ...` line
        for index, line in enumerate(content):
            if line.startswith(b'__version__'):
                old_version = content[index]
                break
        else:
            old_version = None

        # Generate new version only if setup is built with "sdist"
        if 'sdist' in sys.argv:  # TODO: could account for 'bdist', ... ?
            # e.g '2020.2.3', '2020.2.3v1', ...
            version = time.strftime('%Y.%-m.%-d', time.localtime()) + revision
            new_version = f'__version__ = {version!r}\n'.encode()

            if old_version is None:
                # `__version__` line was not found, so lets add it to the bottom of the page.
                content.append(new_version)
            else:
                content[index] = new_version

            # write updated content
            file.seek(0)
            file.writelines(content)
            file.truncate()
        else:
            # use version number from current `__init__.py` file.
            version = parse_version(old_version)

    return version
