"""25.	In English, the present participle is formed by adding the suffix -ing to the infinite
form: go -> going. A simple set of heuristic rules can be given as follows:
 .               If the verb ends in e, drop the e and add ing
 (if not exception: be, see, flee, knee, etc.)
a.	If the verb ends in ie, change ie to y and add ing
b.	For words consisting of consonant-vowel-consonant, double the final letter before adding ing
c.	By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive
form returns its present participle form. Test your function with words such as lie, see,
move and hug. However, you must not expect such simple rules to work for all cases."""

def make_ing_form(verb):
    new_verb=""
    if(verb.endswith("e")):
        if(verb=="be" or verb=="see" or verb=="flee" or verb=="knee"):
            return verb+"ing"
        else:
            new_verb=verb.removesuffix("e")+"ing"
            return new_verb
    elif(verb.endswith("ie")):
        new_verb=verb.removesuffix("ie")+"y"+"ing"
    else:
        co_vo_co=""
        vowel="aeiou"
        for i in verb:
            if(i in vowel):
                co_vo_co+="vo"
            else:
                co_vo_co+="co"
        if("covoco" in co_vo_co):
            return verb+verb[len(verb)-1]+"ing"
        else:
            return verb+"ing"
def main():
    while(7==7):
        verb=input("Please verb in infinitive:")
        print(make_ing_form(verb))
main()
    
            
