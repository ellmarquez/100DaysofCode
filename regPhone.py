import re
phoneReg = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
number=phoneReg.search('My number is 012-345-6789')
print ('Phone number found: ' +number.group())
print ('The area code is' + number.group(1))