from chessboard import ChessBoard
import movegen

def main():
    # NOTE: currently doesn't validate move or stop at checkmate, just plays
    # This is really just for generating example game gif
    board = ChessBoard()
    board.init_game()
    
    legal_moves = movegen.gen_legal_moves(board)
    print(legal_moves)


if __name__ == "__main__":
    main()
