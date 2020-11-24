from copy import deepcopy

class CSP(object):
    """Class untuk menampung semua keperluan algoritma CSP"""

    board_answer = [[]]
    total_person = 0
    healthy_people = 0
    sick_people = 0
    remainding_people = 0
    result = False

    def __init__(self, board, healthy_people, sick_people):
        self.board = board
        self.healthy_people = healthy_people
        self.sick_people = sick_people

    def _print_solution(self):
        for i in range(len(self.board_answer)):
            print("".join(self.board_answer[i]))

    def _is_safe(self, board, row, col):
        """
        Tes langkah King (Orang Sehat)
        """
        steps = [-1, 0, 1]
        for a in steps:
            for b in steps:
                if row + a < 0 or row + a >= len(board) or col + b < 0 or col + b >= len(board):
                    continue
                else:
                    if board[row + a][col + b] == "X":
                        return False
        return True

    def _check_coor(self, row, col, move_method) -> (int, int):
        """
        Fungsi untuk cek koordinat pergerakan pointer
        karena kita menggunakan 4 arah.
        """
        length = len(self.board)
        if move_method == 0:  # kiri atas
            if col >= length:
                col = 0
                row += 1
        
        elif move_method == 1:  # kanan atas
            if col < 0:
                col = length - 1
                row += 1

        elif move_method == 2:  # kiri bawah
            if col >= length:
                col = 0
                row -= 1

        elif move_method == 3:  # kanan bawah
            if col < 0:
                col = length - 1
                row -= 1

        return row, col

    def _move_pointer(self, board, row, col, move_method, counter):
        """
        Fungsi untuk meng-handle pergerakan pointer sesuai dengan
        move method nya
        """
        if move_method == 0 or move_method == 2:
            return self.CSP(board, row, col + 1, move_method, counter)
        
        elif move_method == 1 or move_method == 3:
            return self.CSP(board, row, col - 1, move_method, counter)

        # return False, counter, main_board

    def _debug_board(self, board):
        for i in range(len(board)):
            print("".join(board[i]))

    # Added graceful stop condition if all people have been positioned
    def CSP(self, main_board, row, col, move_method, counter):
        length = len(main_board)

        # Cek koordinat. Pindahkan pointer ke baris baru dan reset kolom
        row, col = self._check_coor(row, col, move_method)

        # Kalau sudah lewat batas, berarti solusi benar
        if row >= length or row < 0 or counter == self.healthy_people:
            return True, counter, main_board

        if main_board[row][col] == "_":
            if self._is_safe(main_board, row, col):
                main_board[row][col] = "X"
                counter += 1

                temp_result, counter_we_get, main_board = self._move_pointer(
                    main_board, row, col, move_method, counter)
                if temp_result == True:
                    return True, counter_we_get, main_board

                # kalau gagal, balikin lagi seperti semula 
                main_board[row][col] = "_"
                counter -= 1
            else:
                return self._move_pointer(main_board, row, col, move_method, counter)

        elif main_board[row][col] == "#":
            return self._move_pointer(main_board, row, col, move_method, counter)

        return False, counter, main_board

    def run(self):
        """
        Function untuk menjalankan alforitma CSP
        """
        board_length = len(self.board)
        start_point = [
            (0, 0),
            (0, board_length - 1),
            (board_length - 1, 0),
            (board_length - 1, board_length - 1)
        ]

        max_total = -1
        best_method = -1
        final_board = [[]]
        final_result = False
        for method in range(4):
            main_board = deepcopy(self.board)
            row, col = start_point[method]
            result, total, board_result = self.CSP(main_board, row, col, method, 0)
            print(f"total using method {method}: {total}")

            if total > max_total and result:
                max_total = total
                best_method = method
                final_board = board_result
                final_result = result

        self.board_answer = final_board
        self.total_person = max_total
        self.remainding_people = self.healthy_people + self.sick_people - max_total
        self.result = final_result


def solve_for_healthy(board, healthy_people, sick_people):
    csp = CSP(board, healthy_people, sick_people)
    csp.run()

    if csp.result == False: 
        print("Solution does not exist")
        return board
    else:
        csp._print_solution()
    
    return csp.board_answer
