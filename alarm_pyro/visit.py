# This is the code that visits the warehouse.
import sys

import Pyro4
import Pyro4.util
from setter import Setter


sys.excepthook = Pyro4.util.excepthook

times = Pyro4.Proxy("PYRONAME:example.times")
setter = Setter("myset")
setter.set(times)
