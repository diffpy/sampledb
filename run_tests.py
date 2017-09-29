#!/usr/bin/env python
import sys
import pytest

if __name__ == '__main__':
    # show output results from every test function
    args = ['-v']
    # show the message output for skipped and expected failure tests
    if len(sys.argv) > 1:
        args.extend(sys.argv[1:])
    print('pytest arguments: {}'.format(args))

    ret = pytest.main(args)
    sys.exit(ret)
