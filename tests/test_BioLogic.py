# -*- coding: utf-8 -*-

import os.path

from nose.tools import ok_, eq_, raises

from .. import MPTfile

testdata_dir = os.path.join(os.path.dirname(__file__), 'testdata')


def test_open_MPT():
    mpt1, comments = MPTfile(os.path.join(testdata_dir, 'bio-logic1.mpt'))
    eq_(comments, [])
    eq_(mpt1.fieldnames, ["mode", "ox/red", "error", "control changes",
                          "Ns changes", "counter inc.", "time/s",
                          "control/V/mA", "Ewe/V", "dq/mA.h", "P/W",
                          "<I>/mA", "(Q-Qo)/mA.h", "x"])


@raises(ValueError)
def test_open_MPT_fails_for_bad_file():
    mpt1 = MPTfile(os.path.join(testdata_dir, 'bio-logic1.mpr'))
