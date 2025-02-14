from collections import deque

def shortestPath_Ali(grid, start=(1, 1), home=(4, 4)):
    
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0

    # Input Validation
    if n == 0 or m == 0:
        return -1, []

    start_row, start_col = start
    home_row, home_col = home

    if not (0 <= start_row < n and 0 <= start_col < m and
            0 <= home_row < n and 0 <= home_col < m and
            grid[start_row][start_col] == 0 and grid[home_row][home_col] == 0):
        return -1, []

    
    dx = [-1, 0, 1, 0]  
    dy = [0, 1, 0, -1]

    
    queue = deque([(start_row, start_col, [start])])  
    visited = set()

    while queue:
        row, col, path = queue.popleft()

        if (row, col) == (home_row, home_col):
            return len(path), path  

        visited.add((row, col))

        for i in range(4):
            new_row = row + dx[i]
            new_col = col + dy[i]

            if (0 <= new_row < n and 0 <= new_col < m and
                    grid[new_row][new_col] == 0 and (new_row, new_col) not in visited):
                new_path = path + [(new_row, new_col)]
                queue.append((new_row, new_col, new_path))

    return -1, []  # No path found


# Example Usage:
if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0],  # Row 1 (Ali starts here if grid is 0-indexed)
        [0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0]  
    ]

    start = (1, 1)
    home = (4, 4)

    path_length, path_coordinates = shortestPath_Ali(grid, start, home)

    if path_length != -1:
        print("Shortest Path Length:", path_length)  
        print("Shortest Path Coordinates:", path_coordinates) 
    else:
        print("No path found.")
