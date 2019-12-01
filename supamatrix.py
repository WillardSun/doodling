supa_matrix = [
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15]
    ],
    [[16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25],
     [26, 27, 28, 29, 30]
    ],
    [[31, 32, 33, 34, 35],
     [36, 37, 38, 39, 40],
     [41, 42, 43, 44, 45]
    ]
]
# Prints a specific number from the super matrix
print(supa_matrix[0][1][2])
# Prints the whole list in the super matrix
for matrix in supa_matrix:
    for row in matrix:
        for item in row:
            print (item)
