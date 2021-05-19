Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and 
performs following opera,on. 
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9) 
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5 
You have to repeat step (1) and (2) un,l you reach 1 or 89. Note that, always your result will reach 
1 or 89 for sure. Input must be a posi,ve number. 
If the opera,on reaches at the end, 89 return True, if opera,on reaches 1 at the end return False"""

def one_or_eight(no):
    strno=str(no)
    while no!= 1 and no !=89:
        if len(strno) == 1:
            no = no*no
            strno=str(no)
        else:
            no=0
            for _ in strno:
                no = no + (int(_)*int(_))
            strno=str(no)
    if no==89:
        return True
    else:
        return False
input=int(input("Enter input: "))
print(one_or_eight(input))
    