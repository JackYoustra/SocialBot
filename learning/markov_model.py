import pykov as pk
import markovify as mk
from markovify.chain import BEGIN, END
from parsing import user
start_str = BEGIN
end_str = END

# takes matrix of lines and then words
def word_model(lines):
    frequency_map = {}
    for line in lines:
        last = (start_str, )
        with_end = line + [end_str]
        for wordv in with_end:
            word = (wordv, )
            map_val = None
            if not last in frequency_map:
                map_val = {}
                frequency_map[last] = map_val
            else:
                map_val = frequency_map[last]
            if word in map_val:
                map_val[word] += 1
            else:
                map_val[word] = 1
            last = word
    return frequency_map
'''
def word_transition_matrix(lines):
    transition = pk.Matrix()
    model = word_model(lines)
    for word, next_words in model.items():
        newmat = pk.Matrix()
        vec = pk.Vector(next_words)
        vec.normalize()
        for next, chance in vec.items():
            newmat += pk.Matrix({(word, next): chance})
        transition += newmat
    return word_transition_matrix()
'''

def word_transition_matrix(lines):
    chain = mk.Chain("", 1, model=lines)
    return chain

def markovify_model(lines, state_size=2):
    line_sentences = [" ".join(line) for line in lines]
    newlines = "\n".join(line_sentences)
    return mk.NewlineText(newlines, state_size)

