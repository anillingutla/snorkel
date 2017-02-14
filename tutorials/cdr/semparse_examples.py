
class Example(object):
    def __init__(self, explanation=None, candidate=None, denotation=None):
        self.explanation = explanation
        self.candidate = candidate
        self.denotation = denotation # True label on this candidate

    def __str__(self):
        return 'Example("%s")' % (self.input)
    
    def display(self):
        print 'Example'
        print('%-12s %s' % ('explanation', self.explanation))
        print('%-12s %s' % ('candidate', self.candidate))
        print('%-12s %d' % ('denotation', self.denotation))


# -7563346943193853808 =>
# "\n \nIt has been almost two years since Klaus Andres, 71, was handed a life 
# sentence for the 2011 killing of wife Li Ping Cao."

test_examples = [
    # Base
    Example(
        explanation="label True because True",
        candidate=('foo', 'bar'),
        denotation=1),
    # And
    Example(
        explanation="label True because True and True",
        candidate=('foo', 'bar'),
        denotation=1),
    # Or
    Example(
        explanation="label True because False or True",
        candidate=('foo', 'bar'),
        denotation=1),
    # Not
    Example(
        explanation="label True because not False",
        candidate=('foo', 'bar'),
        denotation=1),
    # Equals (String)
    Example(
        explanation="label True because 'yes' equals 'yes'",
        candidate=('foo', 'bar'),
        denotation=1),
    # Equals (Int)
    Example(
        explanation="label True because 1 is equal to 1",
        candidate=('foo', 'bar'),
        denotation=1),
    # Integers (digit or text)
    Example(
        explanation="label True because 1 is equal to one",
        candidate=('foo', 'bar'),
        denotation=1),
    # Less than
    Example(
        explanation="label True because 1 is less than 2",
        candidate=('foo', 'bar'),
        denotation=1),
    # At most
    Example(
        explanation="label True because 2 is less than or equal to 2",
        candidate=('foo', 'bar'),
        denotation=1),
    # Greater than
    Example(
        explanation="label True because 2 > 1",
        candidate=('foo', 'bar'),
        denotation=1),
    # At least
    Example(
        explanation="label True because 2 is at least 2",
        candidate=('foo', 'bar'),
        denotation=1),
    # Lowercase
    Example(
        explanation="label True because the word arg 1 is lowercase",
        candidate=('foo', 'bar'),
        denotation=1),
    # Uppercase
    Example(
        explanation="label True because the word arg 1 is upper case",
        candidate=('FOO', 'bar'),
        denotation=1),
    # Capitalized
    Example(
        explanation="label True because the arg 1 is capitalized",
        candidate=('Foo', 'bar'),
        denotation=1),
    # Starts with
    Example(
        explanation="label True because the word 'blueberry' starts with 'blue'",
        candidate=('foo', 'bar'),
        denotation=1),
    # Ends with
    Example(
        explanation="label True because the word 'blueberry' ends with 'berry'",
        candidate=('foo', 'bar'),
        denotation=1),
    # Candidate as string
    Example(
        explanation="label True because argument 1 is 'foo'",
        candidate=('foo', 'bar'),
        denotation=1),
    # In
    Example(
        explanation="label True because 'bar' is in 'foobarbaz'",
        candidate=('foo', 'bar'),
        denotation=1),
    # Contains
    Example(
        explanation="label True because the word 'foobarbaz' contains 'oobarba'",
        candidate=('foo', 'bar'),
        denotation=1),
    # List
    Example(
        explanation="label True because 'bar' is in the list ('foo','bar','baz')",
        candidate=('foo', 'bar'),
        denotation=1),
    # Left words
    Example(
        explanation="label True because 'wife' is in the words left of arg 2",
        candidate=-7563346943193853808,
        denotation=1),    
    # Right words
    Example(
        explanation="label True because 'wife' is in the words to the right of arg 1",
        candidate=-7563346943193853808,
        denotation=1),    
    # Between words
    Example(
        explanation="label True because 'wife' is between arg 1 and arg 2",
        candidate=-7563346943193853808,
        denotation=1),    
    # NER tags
    Example(
        explanation="label True because a person is to the left of arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    # POS tags
    Example(
        explanation="label True because a noun is between arg 1 and arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    # Count
    Example(
        explanation="label True because the number of words between arg 1 and arg 2 is less than 20",
        candidate=-7563346943193853808,
        denotation=1),
    # Index
    Example(
        explanation="label True because the first word to the left of arg 2 equals 'wife'",
        candidate=-7563346943193853808,
        denotation=1),
    # Slice0
    Example(
        explanation="label True because 'wife' is within two words to the left of arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    # # Slice1
    # Example(
    #     explanation="label True because 'part' is within two words to the right of arg 2",
    #     candidate=-7563346943193853808,
    #     denotation=1),
    # # Slice2
    # Example(
    #     explanation="label True because 'lawyer' is within two words of arg 1",
    #     candidate=-7563346943193853808,
    #     denotation=1),
    # # Slice3
    # Example(
    #     explanation="label True because the 'lawyer' is more than two words away from arg 2",
    #     candidate=-7563346943193853808,
    #     denotation=1),
    # Merge
    Example(
        explanation="label True because 'wife' is to the left of arg 1 or arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    # Intersection0
    Example(
        explanation="label True because there is at least one word from colors in the bluebird words",
        candidate=('foo', 'bar'),
        denotation=1),
    # Intersection1
    Example(
        explanation="label False because less than two colors words are in bluebird",
        candidate=('foo', 'bar'),
        denotation=-1),
    # Disjoint
    Example(
        explanation="label True because there are no colors words in the greek words",
        candidate=('foo', 'bar'),
        denotation=1),
    # All
    Example(
        explanation='label True because all of the colors are lowercase',
        candidate=('foo', 'bar'),
        denotation=1),
    # Any
    Example(
        explanation='label True because any of the words letters are lowercase',
        candidate=('foo', 'bar'),
        denotation=1),
    # None
    Example(
        explanation='label True because none of the smalls are capitalized',
        candidate=('foo', 'bar'),
        denotation=1),
    # Sentence
    Example(
        explanation='label True because the word "wife" is in the sentence',
        candidate=-7563346943193853808,
        denotation=1),
    # Composition0
    Example(
        explanation="label True because 'wife' is between arg 1 and arg 2 and 'years' is to the left of arg 1",
        candidate=-7563346943193853808,
        denotation=1),
    # Composition1
    Example(
        explanation="label True because arg 1 is identical to arg 2",
        candidate=('foo', 'foo'),
        denotation=1),
    # Composition2
    Example(
        explanation="label True because there is at least one spouse word between arg 1 and arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    # Composition3
    Example(
        explanation="label True because there is at least one spouse word within two words to the left of arg 1 or arg 2",
        candidate=-7563346943193853808,
        denotation=1),
]


spouse_examples = [
#     explanations = [
#     "Label false because the number of words between arg 1 and arg 2 is larger than 10",
#     "Label false because there is a person between arg 1 and arg 2",
#     "Label true because there is at least one spouse word in the words between arg 1 and arg 2",
#     "Label true because there is at least one spouse word within two words to the left of arg 1 or arg 2",
#     "Label false because there are no spouse words in the sentence",
#     "Label true because the word 'and' is between arg 1 and arg 2 and 'married' is to the right of arg 2",
#     "Label false because there is at least one family word between arg 1 and arg 2",
#     "Label false because there is at least one family word within two words to the left of arg 1 or arg 2",
#     "Label false because there is at least one coworker word between arg 1 and arg 2",
#     "Label false because arg 1 is identical to arg 2",
#     ]
    Example(
        explanation="Label false because the number of words between arg 1 and arg 2 is larger than 10",
        candidate=-5729816328165410632,
        denotation=-1),
    Example(
        explanation="Label false because there is a person between arg 1 and arg 2",
        candidate=-8692729291220282012,
        denotation=-1),
    Example(
        explanation="Label true because there is at least one spouse word in the words between arg 1 and arg 2",
        candidate=-3135315734051751361,
        denotation=1),
    Example(
        explanation="Label true because there is at least one spouse word within two words to the left of arg 1 or arg 2",
        candidate=-7563346943193853808,
        denotation=1),
    Example(
        explanation="Label false because there are no spouse words in the sentence",
        candidate=-8021416815354059709,
        denotation=-1),
    Example(
        explanation="Label true because the word 'and' is between arg 1 and arg 2 and 'married' is to the right of arg 2",
        candidate=None,
        denotation=1),
    Example(
        explanation="Label false because there are no spouse words in the sentence",
        candidate=-8021416815354059709,
        denotation=-1),
    Example(
        explanation="Label false because there is at least one family word between arg 1 and arg 2",
        candidate=-8692729291220282012,
        denotation=-1),
    Example(
        explanation="Label false because arg 1 is identical to arg 2",
        candidate=660552142898381681,
        denotation=-1),
]


cdr_examples = [
    Example(
        explanation="Label false because arg 1 ends with 'induced'",
        candidate=('blue-induced', 'coma'),
        denotation=-1),
    # Example(
    #     explanation="Label false because any between arg 1 and arg 2 ends with '-induced'",
    #     candidate=None,
    #     denotation=-1),
]


def get_examples(which, candidates):
    if which=='test':
        examples = test_examples
    elif which=='spouse':
        examples = spouse_examples
    elif which=='cdr':
        examples = cdr_examples
    else:
        raise Exception("Invalid example set provided.")
    
    candidate_dict = {hash(c) : c for c in candidates}
    for example in examples:
        if example.candidate and not isinstance(example.candidate, tuple):
            example.candidate = candidate_dict[hash(example.candidate)]
    # assert(example.candidate is not None for example in examples)
    return examples