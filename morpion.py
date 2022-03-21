def morpion():
    start = True
    def aff(coord):
        if n % 2 == 0:
            P[coord] = "X"
            print(" _",P[0],"_|_",P[1],"_|_",P[2],"_","\n","_",P[3],"_|_",P[4],"_|_",P[5],"_\n ","",P[6]," | ",P[7]," | ",P[8]," ")
        else:
            P[coord] = "0"
            print(" _",P[0],"_|_",P[1],"_|_",P[2],"_","\n","_",P[3],"_|_",P[4],"_|_",P[5],"_\n ","",P[6]," | ",P[7]," | ",P[8]," ")
    P = ["_","_","_","_","_","_"," "," "," "]
    n = 0
    while start:
        n+= 1
        val = int(input("rentre une valeur de 0 - 9 "))
        aff(val)
        if n > 9:
            print("égalité")
            start = False
            
        """En Construction"""
#         elif P[0] == "X" and P[4] == "X" and P[9] == "X" or P[0] == "O" and P[4] == "O" and P[9] == "O":
#             start = False
#             
#         elif P[2] == "X" and P[4] == "X" and P[6] == "X" or P[2] == "O" and P[4] == "O" and P[6] == "O":
#             start = False
#             
#         elif P[0] == "X" and P[1] == "X" and P[2] == "X" or P[0] == "O" and P[1] == "O" and P[2] == "O":
#             start = False
#             
#         elif P[3] == "X" and P[4] == "X" and P[5] == "X" or P[3] == "O" and P[4] == "O" and P[5] == "O":
#             start = False
#         
#         elif P[6] == "X" and P[7] == "X" and P[8] == "X" or P[6] == "O" and P[7] == "O" and P[8] == "O":
#             start = False
#             
#         elif P[0] == "X" and P[3] == "X" and P[6] == "X" or P[0] == "O" and P[3] == "O" and P[6] == "O":
#             start = False
#             
#         elif P[1] == "X" and P[4] == "X" and P[7] == "X" or P[1] == "O" and P[4] == "O" and P[7] == "O":
#             start = False
#             
#         elif P[2] == "X" and P[5] == "X" and P[8] == "X" or P[2] == "O" and P[5] == "O" and P[8] == "O":
#             start = False
            
        