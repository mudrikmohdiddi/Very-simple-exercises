"""20.	Represent a small bilingual lexicon as a Python dictionary
in the following fashion {"merry":"god", "christmas":"jul",
"and":"och", "happy":gott", "new":"nytt", "year":"år"} and
use it to translate your Christmas cards from English into
Swedish. That is, write a function translate() that takes a list
of English words
and returns a list of Swedish words."""

def translate(english):
    dictionary={"merry":"god", "christmas":"jul","and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    swedish=[]
    for i in english:
        try:
            swedish.append(dictionary[i])
        except KeyError:
            return "You word which does not obtain in dictionary"
    return swedish    
def main():
    english=input("Enter  english list word:")
    while((" " in english) or ("," not in english)):
        print("Invalidy input")
        english=input("Enter  english list word:")
    print(translate(english.split(",")))
main()
    
    
