import blaze as bz
import numpy as np
import bcolz as bc
from blaze import Data, compute

_blaze = Data("/home/rcanseco/PycharmProjects/mysql-petl-bcolz/bcolz_data.bcolz")
print _blaze.fields
print _blaze.data
v = _blaze['count']
print  v.fields