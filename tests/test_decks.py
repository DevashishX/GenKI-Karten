from pathlib import Path
import decks
import utils
import explanation
DECK_PATH =  Path(r"D:\GenkiKarten\decks\TEST.txt")
WRITE_PATH = Path(r"D:\GenkiKarten\decks\TEST_WRITE.txt")


def test_deck():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    print(deck_df.head())
    print(deck_df.columns)
    assert not deck_df.empty, "Deck is empty"
    assert deck_df.shape[0] == 116

def test_write_deck():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    deck_df.to_csv(WRITE_PATH, sep="\t", index=False, header=False)
    assert WRITE_PATH.exists(), "Deck file does not exist after writing"
    print(f"Deck written to {WRITE_PATH}")
    