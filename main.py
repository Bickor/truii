import api

def main():
    board = api.getMemberBoardsNames()[0]
    print(board["name"])
    board_list_0 = api.getListsOnBoard(board["id"])[0]
    print(board_list_0)
    list_card_0 = api.getCardsOnList(board_list_0["id"])
    print(list_card_0[0]["name"])

main()