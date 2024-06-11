
"""
You are given coordinates, a string that represents coordinates of square of chessboard.
Return True if square is white , & False if square is black.
The coordinates will always represent valid chessboardsquare.
The coordinates will always have letter first, & number second.
"""
even_rows="2468"
odd_rows="1357"
even_columns="bdfh"
odd_columns="aceg"
s="h6"
if s[0] in even_columns:
    if s[1] in even_rows:
           print("Black")
    else:
        print("White")
else:
    if s[1] in even_rows:
        print("White")
    else:
        print("Black")
#Output : Black
