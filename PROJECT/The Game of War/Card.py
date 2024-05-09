#Updated
rank_dict = {
    1: "Ace",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King"
}

suit_dict = {
    1: "Spades",
    2: "Hearts",
    3: "Clubs",
    4: "Diamonds"
}


class Card:
    def __init__(self, rank: int, suit: int):
        self.rank: int = self.set_rank(rank)
        self.rank_name: str = rank_dict[self.rank]
        self.suit: int = self.set_suit(suit)
        self.suit_name: str = suit_dict[self.suit]

    @staticmethod
    def set_rank(rank: int) -> int:
        if rank in rank_dict:
            return rank
        return 2  # fail soft

    @staticmethod
    def set_suit(suit: int) -> int:
        if suit in suit_dict:
            return suit
        return 1  # fail soft

    def declare_name(self) -> str:
        return self.rank_name + " of " + self.suit_name
