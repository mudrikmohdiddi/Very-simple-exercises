"""23.	The third person singular verb form in English is distinguished by the suffix -s,
which is added to the stem of the infinitive form: run -> runs.
A simple set of rules can be given as follows:
a.	If the verb ends in y, remove it and add ies
b.	If the verb ends in o, ch, s, sh, x or z, add es
c.	By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive
form returns its third person singular form. Test your function with words like try,brush,run and fix. Note however that the rules must be regarded as heuristic,
in the sense that you must not expect them to work for all cases.
Tip: Check out the string method endswith()."""

def make_3sg_form(word):
    verb_end=["o","ch","s","sh","x","z"]
    new_word=word
    if(word.endswith("y")):
        new_word=""
        for i in range(len(word)-1):
            new_word+=word[i]
        new_word+="ies"
        return new_word
    else:
        sum=0
        for i in verb_end:
            if(word.endswith(i)):
                new_word=word+"es"
            else:
                sum+=1
        if((sum==6) and (new_word==word)):
            return word+"s"
        else:
            return new_word
def main():
    while(5==5):
        word=input("Please enter verb in infinitive:")
        print(make_3sg_form(word))
main()    




