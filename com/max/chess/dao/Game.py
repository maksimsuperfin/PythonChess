class Game():
    dict_players_colors = {}
    cells = [[0 for i in range(8)] for j in range(8)]

    __first_row_idx = 0
    __last_row_idx = 8
    __first_col_idx = 0
    __last_col_idx = 8

    def __init__(self, player1, player2, color1="white", color2="black", cells = []):
        self.player1 = player1
        self.dict_players_colors[player1] = color1
        self.player2 = player2
        self.dict_players_colors[player2] = color2
        if len(cells) == 0:
            self.init_desk()

    def init_desk(self):
        print("Desk: init_desk")

        for row in range(self.__first_row_idx + 2, self.__last_row_idx - 2):
            #self.cells.append([])
            for column in range(self.__first_col_idx, self.__last_col_idx):
                self.cells[row][column] = "0"
                #print(self.cells[row][column])
        for row in range(self.__first_row_idx, self.__first_row_idx + 2):
            #self.cells.append([])
            for column in range(self.__first_col_idx, self.__last_col_idx):
                self.cells[row][column] = "1"
        for row in range(self.__last_row_idx - 2, self.__last_row_idx):
            #self.cells.append([])
            for column in range(self.__first_col_idx, self.__last_col_idx):
                self.cells[row][column] = "-1"


    def current_position(self):
        print("Desk: current_position")
        for player in self.dict_players_colors.keys():
            print(player.name + " is " + self.dict_players_colors[player])
        self.display_dash_board()

    def display_dash_board(self):
        print("Desk: display_dash_board")
        for row in range(self.__last_row_idx):
            row_of_desk = ""
            for column in range(self.__last_col_idx):
                row_of_desk = row_of_desk + " " + str(self.cells[row][column])
            print(row_of_desk)