# Quizbowl-Bot
HIGH-LEVEL OBJECTIVE: The goal of this project is to create a bot that can successfully answer high-school level quizbowl questions. 
### For Those Unframiliar with Quizbowl
Quizbowl is a form of academic competition in which two teams of four compete against each other on a set of 20 questions. These questions range in length from four to eight sentences long. Well-written questions get easier as the question progresses, meaning the most obscure information appears in the first sentence of the question, and each subsequent sentence contains more and more "common knowledge" information. In a tournament questions are read aloud by a moderator, and players can answer at any point while the question is being read. Generally, the earlier one is able to answer a given question, the more one knows about the given topic. Take the following example from a high-school tournament:

> QUESTION: In this novel, Walter Cunningham is offered a quarter to buy lunch, but his teacher Miss Caroline fails to understand that he'll never be able to pay her back; later, Burris attends his one annual day of school. The narrator sees Link Deas and Mr. Raymond exhibit unusual sympathy, and she finally meets the recluse Boo Radley after an altercation in which, according to the sheriff, Bob Ewell fell on his own knife. For 10 points, identify this novel featuring the lawyer Atticus Finch and the young narrator Scout, a semi-autobiographical work written by Harper Lee.

> ANSWER: To Kill a Mockingbird

This question obviously falls under the topic "literature". In a standard round of 20 questions, the distribution of topics is fixed:
  - Science (4 questions)
  - History (4 questions)
  - Literature (4 questions)
  - Fine Arts (3 questions)
  - Philosophy/Social Science (2 questions)
  - Religion (1 question)
  - Mythology (1 question)
  - Geography (1 question)
  
Within each of these topics, question writers can choose to write about anything they want. A literature question can be written on any author to ever publish fiction, including ones that are extremely obscure. However, question writers usually limit the set of topics they ask about based on the intended difficulty of the tournament. A novice-level high school tournament is not going to have a question on _At Swim-Two-Birds_, for example.

Eventually, we would like to build a bot that can determine the answer to a given question. One of the main challenges in accomplishing this is the fact that the set of possible answers to a question is enormous. In an attempt to narrow this set down to a manageable level, our bot will first narrow down questions to their topic categories before searching for an answer. This means we need a classifier that accepts a question as input and outputs one of the eight categories listed above. That is the stage of the project we are currently working on, and what the rest of this document is about. 

### Mechanics of the Project
The input data for our project is a set of around 50,000 quizbowl questions that have appeared in tournaments over the past ten years. Each one of these questions comes with a label indicating the topic area the question belongs to. All of these labels were determined by human beings, menaing a human read each question and assigned it to one of the eight categories above. Imagine you were asked to generate a topic label for the question shown earlier without knowing what the answer was. It would be relatively easy for you to assign a topic label based on the vocabulary of the question; the one above uses the words "novel", "written", "narrator", etc., which indicate that the question is related to literature. History questions are likely to feature words like "battle", "leader", "empire", and so on. Each topic has its own set of identifying words that humans can easily use to categorize questions. 

These identifying words are meaningful to you as a human being because you have spent a lifetime building up a vocabulary of the English language. You have repeatedly heard the word "novel" used in conjuction with other words related to literature, so your brain has built a model that ties these concepts together. The word "protein" is included in a different mental model that connects words related to science. Note that you are not born with any of these liguistic relationships pre-loaded into your brain. Instead, you experience the use of these words in context over and over again until you internalize their relationships to one another. The NLP techniques used in this project operate in a very similar way. 

In the same way that your ability to categorize questions is based on a lifetime of experiencing language, the classifier used in this project chooses category labels based on a large set of training data that it has studied in the past. We train the classifier on around 40,000 "example" questions, meaning we show the classifier each question and the category label that that question _should_ be assigned. The classifier then studies the relationship between the words used in the questions and their category labels. If a given word frequently appears in questions labeled history and never appears in questions labeled mythology, the classifier learns that it should pick the label history and not mythology whenever it encounters that word. In this way, the classifier learns what words are associated with what categories. Then, when you present the classifier with a new question it has never seen before, it can apply everything it learned from the training set and predict the category of the new question.
