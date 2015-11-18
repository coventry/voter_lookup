# Takes a couple of hours to run.  Be sure to have a hotswap...

import os
from . import index_voters

assert not os.system('apt-get install libxapian-dev python-xapian git zip')
assert not os.system('wget ftp://sosftp.sos.state.oh.us/free/Voter/SWVF_1_44.zip')
assert not os.system('wget ftp://sosftp.sos.state.oh.us/free/Voter/SWVF_45_88.zip')
assert not os.system('for p in SWVF_*.zip ; do unzip $p ; done')

index_voters.main()
