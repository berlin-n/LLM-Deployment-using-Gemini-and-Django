from Candidate import Candidate
from GeminiGenerator import GeminiGenerator

class CoverLetterService:
    def __init__(self, generator: GeminiGenerator):
        self.generator = generator

    def generateCoverLetter(self, candidate: Candidate):
        prompt = candidate.generatePrompt()
        return self.generator.generate(prompt)

    def generateTokenUsage(self, candidate: Candidate):
        prompt = candidate.generatePrompt()
        return self.generator.generateOnlyTokenUsage(prompt)
    