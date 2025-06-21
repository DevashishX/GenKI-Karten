import pytest
from pathlib import Path
import decks
import utils
import explanation
from dotenv import load_dotenv
from os import getenv
DECK_PATH =  Path(r"D:\GenkiKarten\decks\TEST.txt")


def test_read_env():
    load_dotenv()
    GENAI = getenv("GENAI", "false")
    if GENAI == "false":
        raise ValueError("GENAI environment variable is not set. Please set it to api key to use this API.")

def test_add_explanation_mock():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    deck_df = deck_df.iloc[:10]  # Limit to first 10 rows for testing
    # use api.add_explanation to add values in the 3rd column
    mockExplanation = explanation.MockExplanation()
    deck_df[3] = deck_df.apply(lambda row: mockExplanation.add_explanation(row[1], row[2]), axis=1)
    # deck_df[3] = deck_df.apply(lambda row: api.add_explanation_mock(row[1], row[2]), axis=1)
    print(deck_df.head(10))

# skip this pytest
@pytest.mark.skip(reason="Skipping test_add_explanation_llm for now")
def test_add_explanation_llm():
    utils.reset_test_deck(DECK_PATH, Path(r"D:\GenkiKarten\decks\TEST.txt.orig"))
    deck_df = decks.load_deck(DECK_PATH)
    deck_df = deck_df.iloc[:2]  # Limit to first 10 rows for testing
    # use api.add_explanation to add values in the 3rd column
    llmExplanation = explanation.GoogleExplanation()
    deck_df[3] = deck_df.apply(lambda row: llmExplanation.add_explanation(row[1], row[2]), axis=1)
    # deck_df[3] = deck_df.apply(lambda row: api.add_explanation_llm(row[1], row[2]), axis=1)
    print(deck_df.head())
    