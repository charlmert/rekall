import logging

# Setup logging as required. Rekall will log to the standard logging service.
logging.basicConfig(level=logging.DEBUG)

from rekall import session
from rekall import plugins                           # 1

s = session.Session(                                 # 2
   filename="win7.elf",
   autodetect=["rsds"],
   logger=logging.getLogger(),
   autodetect_scan_length=18446744073709551616,       # 3
   profile_path=[
      "http://profiles.rekall-forensic.com"
   ])

print s.plugins.pslist(method="PsActiveProcessHead")
