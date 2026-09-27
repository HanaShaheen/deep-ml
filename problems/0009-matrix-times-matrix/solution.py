def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    
    if len(a[0])!=len(b):
        return -1

    rows_a,cols_a=len(a), len(a[0])
    cols_b=len(b[0])

    # c should have s many rows as a has and columns as b
    #columns are per row, so row is outer loop

    c=[ [0 for _ in range(cols_b)] for _ in range(rows_a) ]

    for i in range(rows_a):
        for j in range(cols_b):
            c[i][j]=sum(a[i][k] * b [k][j] for k in range(len(b))) 

    
    return c