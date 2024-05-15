width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)


width_top = ('#'*(int(width/2)) + '-'*(int(width/2)) + '\n')
width_bottom = ('-'*(int(width)) + '\n')

flag = width_top * int(height / 2) + width_bottom * int(height/2)
print(flag)