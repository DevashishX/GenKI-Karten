import pandas as pd

def load_deck(deck_path):
    deck_df = pd.read_csv(deck_path, sep="\t", header=None, skiprows=4)
    if deck_df.empty:
        raise ValueError("Deck is empty")
    return deck_df
