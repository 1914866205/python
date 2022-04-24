def move(layers, A, B, C):
    if layers == 1:
        print(A, "->", C)
        return
    move(layers - 1, A, C, B)
    move(1, A, B, C)
    move(layers - 1, B, A, C)


move(3, "A", "B", "C")
