# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Test invocation of datalad utilities "as is installed"
"""

from .utils import ok_startswith, eq_, \
    ignore_nose_capturing_stdout, assert_cwd_unchanged

from datalad.cmd import Runner

def check_run_and_get_output(cmd):
    runner = Runner()
    status, output = runner.run(["datalad", "--help"], return_output=True)
    if status:
        raise AssertionError("'datalad --help' failed to start normally. "
                             "Exited with %d and output %s" % (status, output))
    return output

@ignore_nose_capturing_stdout
@assert_cwd_unchanged
def test_run_datalad_help():
    out, err = check_run_and_get_output("datalad --help")
    ok_startswith(out, "Usage: ")
    eq_(err, "")