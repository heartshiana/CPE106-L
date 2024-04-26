
import random

def get_words(filename):
    """Reads words from the specified file and returns them as a tuple."""
    with open(filename) as file:
        words = tuple(line.strip() for line in file)
    return words

def sentence():
    """Builds and returns a sentence."""
    return noun_phrase() + " " + verb_phrase()

def noun_phrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verb_phrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + noun_phrase() + " " + prepositional_phrase()

def prepositional_phrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + noun_phrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input('Enter number of sentences: '))
    for count in range(number):
        print(sentence())

if __name__ == '__main__':
    articles = get_words('articles.txt')
    nouns = get_words('nouns.txt')
    verbs = get_words('verbs.txt')
    prepositions = get_words('prepositions.txt')
    main()


