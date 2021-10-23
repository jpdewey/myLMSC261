stack = int(input('Choose a number between 1 and 8 for pyramid height: '))
for i in range(1):
    if stack == 1:
        print('#')
    elif stack == 2:
        print(' #\n##')
    elif stack == 3:
        print('  #\n ##\n###')
    elif stack == 4:
        print('   #\n  ##\n ###\n####')
    elif stack == 5:
        print('    #\n   ##\n  ###\n ####\n#####')
    elif stack == 6:
        print('     #\n    ##\n   ###\n  ####\n #####\n######')
    elif stack == 7:
        print('      #\n     ##\n    ###\n   ####\n  #####\n ######\n#######')
    elif stack == 8:
        print('       #\n      ##\n     ###\n    ####\n   #####\n  ######\n #######\n########')
    else:
        print('Number is out of range. Sorry!')
        
