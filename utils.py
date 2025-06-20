from pathlib import Path

# a function which replaces TEST.txt with a copy of TEXT.txt.orig on disk
import shutil
def reset_test_deck(test_deck_path: Path, original_deck_path: Path):
    """
    Resets the test deck by copying the original deck file to the test deck path.
    
    :param test_deck_path: Path to the test deck file (e.g., TEST.txt).
    :param original_deck_path: Path to the original deck file (e.g., TEXT.txt.orig).
    """
    shutil.copy(original_deck_path, test_deck_path)
    print(f"Test deck reset: {test_deck_path} has been replaced with {original_deck_path}.")
