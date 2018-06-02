#! python3
#pw.py password locker 
# No, they are not real passwords! 
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01MLZF3sdt',
             'luggage': '123459'}

import sys
if len(sys.argv) <2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account=sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for: '+ account +' coppied to clipboard')
else:
    print ('Password for ' +account +' not found')