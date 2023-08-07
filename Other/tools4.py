
# Call Linux commands out of the Python

import sh

print(sh.ls('/home'))
print(sh.pwd)
print(sh.whoami)

sh.mkdir('result')
sh.touch('result/result.txt')

