import chess
import random
import time

# Initialize the board
board = chess.Board()


# Define evaluation function
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


# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    if maximizing_player:
        max_eval = float('-inf')
        for move in get_legal_moves(board):
            board.push(chess.Move.from_uci(move))
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_legal_moves(board):
            board.push(chess.Move.from_uci(move))
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Choose the best move for AI agent
def choose_move(board, depth):
    best_move = None
    max_eval = float('-inf')
    for move in get_legal_moves(board):
        board.push(chess.Move.from_uci(move))
        eval = minimax(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move


# Make a random move for the computer player
def make_random_move(board):
    legal_moves = list(board.legal_moves)
    random_move = random.choice(legal_moves)
    board.push(random_move)


# Play a game against the AI agent
while not board.is_game_over():
    if board.turn == chess.WHITE:
        # AI agent's turn
        print("AI agent is thinking...")
        time.sleep(3)  # Delay of 3 seconds
        move = choose_move(board, 5)  # Depth of 2 for minimax search
        print("AI agent chooses move:", move)
        board.push(chess.Move.from_uci(move))
    else:
        time.sleep(3)
        # Computer player's turn
        make_random_move(board)
        print("Computer player chooses move.")

    print(board)

print(board.result())