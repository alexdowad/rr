from util import *
import re

send_gdb('info threads')
expect_gdb(r'1\s+Thread \d+\.\d+ \(simple-[A-Za-z0-9]+\)')

ok()
