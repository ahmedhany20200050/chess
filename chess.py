import chess

def evaluate_board(board):
    # Simple evaluation function that just counts the material difference
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 1000
    }
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = piece_values[piece.piece_type]
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    return score

# Generate legal moves
def get_legal_moves(board):
    legal_moves = []
    for move in board.legal_moves:
        legal_moves.append(str(move))
    return legal_moves