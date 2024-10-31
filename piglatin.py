class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase
        translator = PigLatin.PigLatin("this is a phrase")
        phrase = translator.get_phrase()
        translation = translator.translate()

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        pass
