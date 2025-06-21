import explanation, decks
from pathlib import Path

if __name__ == "__main__":
    DECK_PATH = Path(r"D:\GenkiKarten\decks\TEST.txt")
    WRITE_PATH = Path(r"D:\GenkiKarten\decks\TEST_WRITE.txt")

    # Load the deck
    deck_df = decks.load_deck(DECK_PATH)
    print(deck_df.head())

    # Add explanations using MockExplanation
    mock_explanation = explanation.MockExplanation()
    deck_df[3] = deck_df.apply(lambda row: mock_explanation.add_explanation(row[1], row[2]), axis=1)

    # Write the updated deck to a new file
    deck_df.to_csv(WRITE_PATH, sep="\t", index=False, header=False)
    print(f"Deck with explanations written to {WRITE_PATH}")