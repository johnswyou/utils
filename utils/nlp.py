import requests
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def get_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        response.raise_for_status()

def get_word_definition(word):
    word_dict = get_word(word)
    return word_dict['meanings'][0]['definitions'][0]['definition']

def get_word_type(word):
    word_dict = get_word(word)
    return word_dict['meanings'][0]['partOfSpeech']

def strip_punctuation(text):
    """Strip punctuation marks from a string"""
    return re.sub(r'[^\w\s]', '', text)

class WordSimilarity:

    """Class for visualizing the similarity between words using GloVe embeddings
    
    Parameters
    ----------
    words : list
        List of words to visualize
    glove_file_path : str
        Path to the GloVe embeddings file (e.g. glove.6B.300d.txt)
        Can download from https://nlp.stanford.edu/projects/glove/ (we only tested using glove.6B.zip)
    seed : int, optional
        Random seed for reproducibility, by default None

    Methods
    -------
    visualize_similarity_PCA()
        Visualize the similarity between words using PCA
    visualize_similarity_TSNE(perplexity=30)
        Visualize the similarity between words using t-SNE

    Properties
    ----------
    words : list
        List of words to visualize

    """

    def __init__(self, words, glove_file_path, seed=None):
        self.seed = seed
        self._words = list(set(words))
        self.glove_file_path = glove_file_path
        self.embeddings = self.load_embeddings()

    def load_embeddings(self):

        if self.seed is not None:
            np.random.seed(self.seed)

        # Load the pre-trained GloVe embeddings from file
        embeddings_index = {}
        with open(self.glove_file_path, encoding='utf-8') as f:
            for line in f:
                values = line.split()
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                embeddings_index[word] = coefs

        # Create a matrix of embeddings for the given words
        embeddings = []
        for word in self._words:
            if word in embeddings_index:
                embeddings.append(embeddings_index[word])
            else:
                # If the word is not in the embeddings file, assign a random vector
                embeddings.append(np.random.rand(300))
        
        return np.array(embeddings)

    def visualize_similarity_PCA(self):
        
        # Apply PCA to reduce the dimensionality of the embeddings to 2D
        pca = PCA(n_components=2)
        pca_embeddings = pca.fit_transform(self.embeddings)
        
        # Plot the embeddings in 2D
        plt.scatter(pca_embeddings[:, 0], pca_embeddings[:, 1])
        for i, word in enumerate(self._words):
            plt.annotate(word, xy=(pca_embeddings[i, 0], pca_embeddings[i, 1]))
        plt.show()

    def visualize_similarity_TSNE(self, perplexity=30):
        
        # Apply t-SNE to reduce the dimensionality of the embeddings to 2D
        if self.seed is not None:
            tsne = TSNE(n_components=2, perplexity=perplexity, random_state=self.seed)
        else:
            tsne = TSNE(n_components=2, perplexity=perplexity)

        tsne_embeddings = tsne.fit_transform(self.embeddings)
        
        # Plot the embeddings in 2D
        plt.scatter(tsne_embeddings[:, 0], tsne_embeddings[:, 1])
        for i, word in enumerate(self._words):
            plt.annotate(word, xy=(tsne_embeddings[i, 0], tsne_embeddings[i, 1]))
        plt.show()

    @property
    def words(self):
        return self._words
    
    @words.setter
    def words(self, words):
        self._words = list(set(words))
        self.embeddings = self.load_embeddings()
