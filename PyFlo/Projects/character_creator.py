def print_head(hair, eye):
    a = hair
    b = eye
    print(a*12)
    print(f"{a}|        |{a}")
    print(f"{a}|  {b}  {b}  |{a}")
    print(" |   /\   |")
    print(" |        |")
    print(" \  '--'  /")
    print("   ------")
    return



def print_body(segment, arm):
    a = (f"{' '*4+'X'*4}\n")
    b = (f"{arm*4}")
    print("     XX")
    print(f"#{b}XX{b}#")
    print("    XXXX")
    print(f"{(a*segment)+(' '*4+'X'*4)}")
    return



def print_legs(segment, shoe):
    a = (f"{' '+'  ||'*2}\n")
    b = shoe
    c = shoe[::-1]
    print("    ====")
    print(f"{(a*segment)+(' '+'  ||'*2)}")
    print(f" {b}  {c}")
    return



def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    segment = (height - 11) // 2
    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe)

main()