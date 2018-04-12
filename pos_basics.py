from nltk.tag.stanford import StanfordPOSTagger
from nltk.tag import CRFTagger
import os
java_path = "/home/nprabhav/Downloads/Packages/jdk1.8.0_91"
os.environ['JAVAHOME'] = java_path


english_postagger = StanfordPOSTagger('/home/nprabhav/Documents/Genesis/Others/nQuery-master/tagger/english-bidirectional-distsim.tagger','/home/nprabhav/Documents/Genesis/Others/nQuery-master/tagger/stanford-postagger.jar')
sentence = "NANDAN SUKTHANKAR PRANAY SANKET DESHMUKH"
print(english_postagger.tag(sentence.split()))
#	op_file = open("output.txt", "w")
"""
with open('lol.txt') as fp:
    for line in fp:
        sentence = line.strip('\n')
        token_array = english_postagger.tag(sentence.split())
        op_file.write("\n".join((str(elem) for elem in token_array)))
        print(sentence)
"""
#ct = CRFTagger()
#print(ct.tag(sentence.split()))
