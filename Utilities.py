import errno
from os import path
import os


class Utilities:

    @staticmethod
    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    @staticmethod
    def safe_open(path, openType):
        ''' Open "path" for writing, creating any parent directories as needed.
        '''
        Utilities.mkdir_p(os.path.dirname(path))
        return open(path, openType)
