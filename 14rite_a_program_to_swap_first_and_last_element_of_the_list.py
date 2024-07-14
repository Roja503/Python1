li=[12,35,9,56,24]
temp=li[0]
li[0]=li[4]
li[4]=temp
print(li)
28)write_a_program_to_print_the_triangle_star_Pattern.py
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
