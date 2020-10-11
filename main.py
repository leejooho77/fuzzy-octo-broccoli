# This is algorithm for Global Alignment of DNA
# 2 DNA references
ref_x = 'ACG'
ref_y = 'CGT'
# size of 2 DNAs
size_x = len(ref_x) + 1
size_y = len(ref_y) + 1
# score points for match, mismatch, insertion, deletion
# insertion: put blank into reference y
# deletion: put blank into reference x
match = 0
mismatch = 2
indel = 2
# NxN grid to track score
grid = [[0]*size_y for _ in range(size_x)]
# initialize grid with indel score
for i in range(1, size_x):
    grid[i][0] = grid[i - 1][0] + indel
for i in range(1, size_y):
    grid[0][i] = grid[0][i - 1] + indel

for x in range(1, len(grid)):
    for y in range(1, len(grid[x])):
        insert_score = grid[x - 1][y] + indel
        delete_score = grid[x][y - 1] + indel
        match_or_mismatch = grid[x - 1][y - 1] + match if (ref_x[x - 1] == ref_y[y - 1]) else grid[x - 1][y - 1] + mismatch
        # get min score
        grid[x][y] = min(insert_score, delete_score, match_or_mismatch)
# print score grid
for i in grid:
    print(i)
# result vars for x and y
result_x = ''
result_y = ''
# traceback
x, y = (size_x - 1, size_y - 1)
while x > 0 and y > 0:
    up = grid[x - 1][y]
    left = grid[x][y - 1]
    diag = grid[x - 1][y - 1]
    if up < left and up < diag:
        result_x = ref_x[x - 1] + result_x
        result_y = '-' + result_y
        x -= 1
    elif left < up and left < diag:
        result_x = '-' + result_x
        result_y = ref_y[y - 1] + result_y
        y -= 1
    else:
        result_x = ref_x[x - 1] + result_x
        result_y = ref_y[y - 1] + result_y
        x -= 1
        y -= 1

if x > 0:
    result_x = ref_x[x - 1] + result_x
    result_y = '-' + result_y
    x -= 1
elif y > 0:
    result_x = '-' + result_x
    result_y = ref_y[y - 1] + result_y
    y -= 1

# print results
print(x, y)
print(ref_x, ref_y)
print(result_x, result_y)