# test
# comen

import sys
# 引数確認
argvs = sys.argv
argc = len(argvs)
if argc != 2:
    print('Usage: # python %s filename', argvs[0])
    quit()
filename = argvs[1]
f = open(filename, 'r')
data = f.read()
f.close()
print(data)
data = data.replace('# ', '')
data = data.replace('\n', ' ')
f = open('test.txt', 'w')
while len(data) > 0:
    priod_index = data.find('.')
    # : !でも改行したい
    sentence = data[0: priod_index + 1]
    f.writelines(sentence + '\n')
    print(sentence)
    data = data[priod_index + 2:]
print('end')
f.close()
