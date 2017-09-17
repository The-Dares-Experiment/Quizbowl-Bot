# PROJECT: 		Quizbowl Bot (The Dares Project)
# TASK:			Classify Questions
# PURPOSE:		Train a Naive Bayes model that classifies questions by category

import json
from random import shuffle
import nltk.classify.util
from nltk.classify.util import apply_features
from nltk.classify import NaiveBayesClassifier
import numpy as np

#####################################################################################
# INPUTS: The file containing all processed questions 								#
# OUTPUTS: A list of lists, where each element is a tossup and its category label	#
# PURPOSE: Read the classifier input data into a list object 						#
#####################################################################################

def read_in_questions(filename):

	inputFileObject = open(filename, 'rU')
	unshuffledQuestions = []

	for line in inputFileObject:
		questionAndLabel = json.loads(line)
		question = questionAndLabel[0]
		question = question.split(' ')
		label = questionAndLabel[1]
		unshuffledQuestions.append((question, label))

	return unshuffledQuestions

#############################################################################################
# INPUTS: A single question, formatted as a list 											#
# OUTPUS: A dictionary of features extracted from the question 								#
# PURPOSE: Extract feature sets from each question 											#
# WARNING: Including too many features may result in a memory error, especially if you are 	#
#			running a 32-bit version of python												#
#############################################################################################

def question_features(question):

	questionLength = len(question)
	dictOfNGrams = {}

	for i in range(questionLength):
		
		monogram = question[i]
		if monogram not in dictOfNGrams:
			dictOfNGrams[monogram] = 1
		else:
			dictOfNGrams[monogram] += 1

		# NOTE: The following section is commented out due to the memory error described in the function description
		'''try:
			bigram = question[i] + " " + question[i+1]
			if bigram not in dictOfNGrams:
				dictOfNGrams[bigram] = 1
			else:
				dictOfNGrams[bigram] += 1
		except:
			pass

		try:
			trigram = question[i] + " " + question[i+1] + " " + question[i+2]
			if trigram not in dictOfNGrams:
				dictOfNGrams[trigram] = 1
			else:
				dictOfNGrams[trigram] += 1
		except:
			pass'''

	return dictOfNGrams

#####################################################################################################################################################

def main():

	# STEP 1: Read in the complete set of processed question-category pairs (labeled input data)
	questionFile = "classifier_input_JSON.txt"
	questions = read_in_questions(questionFile)

	# STEP 2: Randomize order, then split question-label pairs into training and testing sets
	shuffle(questions)
	trainingCutoff = int(len(questions) * 0.75)
	trainingSet = questions[:trainingCutoff]
	testingSet = questions[trainingCutoff:]

	# STEP 3: Extract features from questions and train/test Naive Bayes model
	trainingSet = apply_features(question_features, trainingSet)
	testingSet = apply_features(question_features, testingSet)
	classifier = NaiveBayesClassifier.train(trainingSet)
	classifier.show_most_informative_features()
	print "accuracy: ", nltk.classify.util.accuracy(classifier, testingSet)

if __name__ == "__main__":
    main()
