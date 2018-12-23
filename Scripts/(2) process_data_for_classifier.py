# PROJECT: 			Quizbowl Bot (The Dares Project)
# TASK:				Process Question Data 
# PURPOSE:			Process question data so it is ready for use in the classifier

import sys
import json
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

# Set Path
rootDir = "...INSERT PATH HERE..." # Modify to local directory
outputDir = rootDir + "\\Temp\\Processed Questions\\"

outputFilename = outputDir + "classifier_input_JSON.txt"
outputFileObject = open(outputFilename, 'w')

# Regular expression used to remove punctuation from text
PUNCTUATION_RE = re.compile(r'[^\w\s]')
# Lemmetizer used to remove word modifiers
lmtzr = WordNetLemmatizer()
# Set of common words to be removed from text
nltkStopWords = set(stopwords.words('english'))
changStopWords = []		# Fill with set of stop words from Chang
stopWords = nltkStopWords

categories = ["fa", "lit", "hist", "sci", "myth", "ps", "rel", "geo"]
	
for category in categories:
	inputFilename = outputDir + category + "_q_answ_JSON.txt"
	inputFileObject = open(inputFilename, 'rU')

	for question in inputFileObject:
		questionUnprocessed = json.loads(question)[0]

		# Remove punctuation
		questionPuncRemoved = re.sub(PUNCTUATION_RE, '', questionUnprocessed).split()

		# Filter out stop words and lemmetize non-stop words
		questionLemmatized = []
		for word in questionPuncRemoved:
			word = word.lower()
			if word not in stopWords:
				lemmatizedWord = lmtzr.lemmatize(word)
				questionLemmatized.append(lemmatizedWord)
		questionLemmatized = ' '.join(questionLemmatized)

		outputFileObject.write(json.dumps((questionLemmatized, category)))
		outputFileObject.write('\n')