#!/usr/bin/env python

import os

from config import Dirs, Files
from utils import xga, read_stderr, get_source_markers, check_errors


# Main test

def runtest():
    """run regression tests"""

    # check for errors
    source = os.path.join(Dirs.gplsources, "gaerrs.gpl")
    with open(Files.error, "w") as ferr:
        xga(source, "-o", Files.output, stderr=ferr, rc=1)
    act_errors = read_stderr(Files.error, include_warnings=False)
    exp_errors = get_source_markers(source, tag=r";ERROR")
    check_errors(exp_errors, act_errors)

    # error messages in pass 0 and 1
    for s in ["gaerrs0.gpl", "gaerrs1.gpl"]:
        source = os.path.join(Dirs.gplsources, s)
        with open(Files.error, "w") as ferr:
            xga(source, "-o", Files.output, stderr=ferr, rc=1)
        act_errors = read_stderr(Files.error, include_warnings=False)
        exp_errors = get_source_markers(source, tag=r"\* ERROR")
        check_errors(exp_errors, act_errors)

    # cleanup
    os.remove(Files.error)


if __name__ == "__main__":
    runtest()
    print "OK"