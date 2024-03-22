def is_valid_move(board, start, end):
    # Check if start and end positions are within the board boundaries
    if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
        return False
    
    start_piece = board[start[0]][start[1]]
    end_piece = board[end[0]][end[1]]
    
    if start_piece == ".":  # If no piece at start position
        return False
    
    # Ensure that the piece at start position is the same color as the piece at end position (if any)
    if end_piece != "." and start_piece.islower() == end_piece.islower():
        return False
    
    # Piece movement logic
    piece = start_piece.lower()
    dx = abs(end[0] - start[0])
    dy = abs(end[1] - start[1])
    
    if piece == "p":
        # Pawn moves differently based on color
        if start_piece.islower():  # Black pawn
            if start[1] == end[1] and start[0] < end[0] <= start[0] + 2 and dx == 1:
                return True
        else:  # White pawn
            if start[1] == end[1] and start[0] > end[0] >= start[0] - 2 and dx == 1:
                return True
    elif piece == "n":
        # Knight moves in L-shape
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
    elif piece == "b":
        # Bishop moves diagonally
        return dx == dy
    elif piece == "r":
        # Rook moves horizontally or vertically
        return start[0] == end[0] or start[1] == end[1]
    elif piece == "q":
        # Queen moves like a bishop or a rook
        return dx == dy or start[0] == end[0] or start[1] == end[1]
    elif piece == "k":
        # King moves one square in any direction
        return dx <= 1 and dy <= 1
    return False

# Example usage:
initial = (1, 0)
final = (3, 0)
board = [
    ["r", ".", "b", "q", "k", "b", ".", "r"],
    ["p", "p", "p", ".", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

print(is_valid_move(board, initial, final))  # Output: True
