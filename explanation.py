import abc
from os import getenv
from dotenv import load_dotenv
load_dotenv()
GENAI = getenv("GENAI", "false")
if GENAI == "false":
    raise ValueError("GENAI environment variable is not set. Please set it to api key to use this API.")
from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List
class Explanation(abc.ABC):
    """
    Abstract base class for explanation generation.
    """
    
    @abc.abstractmethod
    def add_explanation(self, front: str, back: str) -> str:
        """
        Generate an explanation for the given front and back.
        
        :param front: The front of the card.
        :param back: The back of the card.
        :return: Explanation as a html string.
        """
        pass

class MockExplanation(Explanation):
    """
    Mock implementation of Explanation for testing purposes.
    """
    mock = "This is a mock explanation.<br>It is not real and is used for testing purposes only."
    
    def add_explanation(self, front: str, back: str) -> str:
        return self.mock

class UsageExamples(BaseModel):
    """
    model for example of usage of the word in front and back
    """
    # german: str  # German words
    # english: str  # English words
    examples: List[List[str]]  # List of german sentencce and its english translation
    
    def __str__(self):
        # return_string = f"{self.german} ({self.english})<br>"
        return_string = "🌻Examples🌻<br>"
        for example in self.examples:
            return_string += f"{example[0]}<br>{example[1]}<br>"
        return return_string.strip()

class GoogleExplanation(Explanation):
    """
    Implementation of Explanation using Google GenAI.
    """
    mock = "This is a mock explanation.<br>It is not real and is used for testing purposes only."
    
    def __init__(self):
        self.client = genai.Client(api_key=GENAI)
        
    
    def add_explanation(self, front: str, back: str) -> str:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents= f"You are a German language teacher whose job is to provide 3 to 6 usage examples of B1 to C1 level for the given German word and its English translation. \
                The usage examples consist of pairs of German sentences and English translation sentences which demonstrate the use of this word in diffrent tenses.\
                    The german word is: '{front}' and \
                        the english translations are: '{back}'.",
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
                temperature=1.0,
                response_mime_type="application/json",
                response_schema=UsageExamples                
            ),
        )
        usage: UsageExamples = response.parsed
        print(usage)
        
        return self.mock