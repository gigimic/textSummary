# Summarization of text

Text summarization refers to the technique of shortening long pieces of text. The intention is to create a coherent and fluent summary having only the main points outlined in the document.

Extractive Summarization is done here. This method relies on extracting several parts, such as phrases and sentences, from a piece of text and stack them together to create a summary. Therefore, identifying the right sentences for summarization is of utmost importance in an extractive method.

The frequency of every word in the document is calculated. This frequency is then used to calculate the value of each sentence. Then the most important sentences are then used to make a summary.
NLTK tokenizer is used here.
