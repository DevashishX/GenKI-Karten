# import pathlib
# import unittest
from pathlib import Path
# import pandas as pd
import decks
import utils
import api
# DECK_PATH = Path("..\decks\German_tough_Vocab\collection.anki21")
DECK_PATH =  Path(r"D:\GenkiKarten\decks\TEST.txt")
# DECK_PATH =  Path(r"D:\GenkiKarten\decks\TEST\collection.anki21")


def test_deck():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    print(deck_df.head())
    print(deck_df.columns)
    assert not deck_df.empty, "Deck is empty"
    assert deck_df.shape[0] == 116

def test_add_explanation():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    deck_df = deck_df.iloc[:10]  # Limit to first 10 rows for testing
    # use api.add_explanation to add values in the 3rd column
    deck_df[3] = deck_df.apply(lambda row: api.add_explanation(row[1], row[2]), axis=1)
    print(deck_df.head(10))
    