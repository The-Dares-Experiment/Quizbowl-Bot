# PROJECT: 			Quizbowl Bot (The Dares Project)
# TASK:				Process Question Data
# PURPOSE: 			Process raw tossup data from quinterest

import wikipedia
import re
import json
import itertools
import sys

# Set Path
rootDir = "...INSERT PATH HERE..." # Modify to local directory
inputDir = rootDir + "\\Input\\"
outputDir = rootDir + "\\Output\\"
tempDir = rootDir + "\\Temp\\"
processedDir = tempDir + "\\Processed Questions\\"

##################################################################################
# INPUTS: A filename; a dictionary 												 #
# OUTPUTS: A list of lists 													     #
# PURPOSE: Creates a list of each tossup's answer line and question 			 #
##################################################################################

def create_question_answer_pairs(filename):

	# Used to remove comments after answer line
	BRACKET_RE = re.compile(r'\[.*')
	PARANTHESES_RE = re.compile(r'\(.*')
	OR_RE = re.compile(r'\s[oO][rR]\s.*')

	questionData = []

	fileObject = open(filename)
	for line in fileObject:

		# Get the question text of a tossup
		if (line[0:8] == 'Question'):
			question = line[10:]
			question = question.replace('\n', '')
			questionData.append(question)

		# Get the answer line of a tossup
		if (line[0:6] == 'ANSWER'):
			answerLine = line[8:]

			# Remove unnecessary comments surrounding the answer line
			answerLine = re.sub(BRACKET_RE, '', answerLine)
			answerLine = re.sub(PARANTHESES_RE, '', answerLine)
			answerLine = re.sub(OR_RE, '', answerLine)
			answerLine = answerLine.replace('\n', '')

			try:
				# Try passing the answer line to wikipedia in order to use its search matching algorithm
				wikipediaResult = wikipedia.search(answerLine)
				wikipediaResult = wikipediaResult[0]
				questionData.append(wikipediaResult)
			except:
				questionData.append(answerLine)

	fileObject.close()

	# Combine the question and answer line for each tossup into a list of lists
	iterableList = iter(questionData)
	questionAnswerPairs = zip(iterableList, iterableList)

	return questionAnswerPairs

#############################################
# INPUTS: A filename, a list of lists		#
# OUTPUTS: None								#
# PURPOSE: Print tossup data to a JSON file #
#############################################

def output_data_to_JSON(filename, questionAnswerPairs):

	# Output the question answer pairs to a JSON file
	outputObject = open(filename, 'w')

	for element in questionAnswerPairs:
		outputObject.write(json.dumps(element))
		outputObject.write('\n')

	outputObject.close()	

#####################################################################################################################################################

def main():

	# Ask user what category to process
	category = raw_input("Enter category (fa|lit|hist|sci|myth|ps|rel|geo|ALL): ")
	if category == "ALL":
		categories = ["fa", "lit", "hist", "sci", "myth", "ps", "rel", "geo"]
	else:
		categories = [category]


	for category in categories:
		# Create a list of data (question, answer line) for each tossup
		unprocessedQuestionsFile = inputDir + "unprocessed_questions_" + category + ".txt"
		questionAnswerPairs = create_question_answer_pairs(unprocessedQuestionsFile)

		# Print the question data to a JSON file
		outputFile = processedDir + category +'_q_answ_JSON.txt'
		output_data_to_JSON(outputFile, questionAnswerPairs)


if __name__ == "__main__":
    main()