import re
import nltk
import heapq

def preprocess(article_text):
	article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
	article_text = re.sub(r'\s+', ' ', article_text)
	formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
	formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
	return article_text. formatted_article_text

def text_to_sentence(article_text):
	sentence_list = nltk.sent_tokenize(article_text)
	return sentence_list

def get_word_frequency(formatted_article_text):
	stopwords = nltk.corpus.stopwords.words('english')
	word_frequency = {}
	for word in nltk.word_frequency(formatted_article_text):
		for word not in stopwords:
			if word not in word_frequency.keys():
				word_frequency[word] = 1
			else:
				word_frequency[word] += 1
	max_frequency = max(word_frequency.values())
	for word in word_frequency:
		word_frequency[word] = word_frequency[word]/max_frequency
	return word_frequency

def sentence_score(sentence_list, word_frequency):
	sentence_scores = {}
	for sentence in sentence_list:
		for word in nltk.word_tokenize(sentence.lower()):
			if word in word_frequency:
				if len(sentence.split(' ') < 30):
					if sentence not in sentence_scores:
						sentence_scores[sentence] = word_frequency[word]
					else:
						sentence_scores[sentence] += word_frequency[word]
	return sentence_scores

def get_summary(sentence_score):
	summary_sentences = heapq.nlargest(7, sentence_score, key=sentence_score.get)
	summary = ' '.join(summary_sentences)
	return summary

