def is_outside(matrix, col, row):
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])


def get_area_size(matrix, row, col, visited):
    if is_outside(matrix, col, row):
        return 0

    if visited[row][col]:
        return 0
    if matrix[row][col] == '*':
        return 0
    visited[row][col] = True
    return 1 + get_area_size(matrix, row - 1, col, visited) + \
           get_area_size(matrix, row + 1, col, visited) + \
           get_area_size(matrix, row, col - 1, visited) + \
           get_area_size(matrix, row, col + 1, visited)


def main():
    matrix = []
    visited = []
    area = []
    r = int(input())
    c = int(input())
    for row in range(r):
        matrix.append(list(input()))
        visited.append([False] * c)

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '*':
                continue
            if visited[i][j]:
                continue
            area_size = get_area_size(matrix, i, j, visited)
            area.append({'row': i, 'col': j, 'size': area_size})

    sorted_area = sorted(area, key=lambda x: (x['size'], -x['row'], -x['col']), reverse=True)
    print(f"Total areas found: {len(sorted_area)}")
    for i,area in enumerate(sorted_area):
        print(f"Area #{i+1} at ({area['row']}, {area['col']}), size: {area['size']}")


if __name__ == '__main__':
    main()
# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--

# 5
# 10
# *--*---*--
# *--*---*--
# *--*****--
# *--*---*--
# *--*---*--
