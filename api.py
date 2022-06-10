import boards
import lists
import cards

# In order to understand all the methods, you must understand trellos format.
# Each member can have multiple boards. A board can have multiple lists. Each
# list can have multiple cards.

#TODO: Add general input checking to each method.
# Get's all the board information with their respective metadata.
def getMemberBoards(metadata=True):
    return boards.get_member_boards(metadata)

# Gets the name of every board owned by member.
def getMemberBoardsNames():
    return boards.get_member_boards_names()

# Gets all the lists on a board.
def getListsOnBoard(board_id):
    return boards.get_lists_on_board(board_id)

# Gets all the cards on a board but only prints each cards' name.
def getCardsOnBoard(metadata=True):
    return boards.get_cards_on_board(metadata)

# Gets the cards on a board with all their metadata.
def getCardsWithMetadataOnBoard():
    return boards.get_cards_with_metadata_on_board()

def getCardsOnList(list_id):
    return lists.get_cards_on_list(list_id)