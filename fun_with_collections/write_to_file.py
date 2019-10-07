f = open('testscores.txt', 'w')
f.write("First Line\n")
input_list = ['1\t', '2\t', '3\t']
f.writelines(input_list)
f.close()