from sklearn.datasets import fetch_20newsgroups
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
data = fetch_20newsgroups()
print(data)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
# print(data.target_names)
categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space',
 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)
model.fit(train.data, train.target)
labels = model.predict(test.data)
from sklearn.metrics import confusion_matrix
def predict_category(s, train=train, model=model):
 pred = model.predict([s])
 return train.target_names[pred[0]]
print(predict_category('sending a payload to the ISS'))
# mat = confusion_matrix(test.target, labels)
# sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=train.target_names,
#             yticklabels=train.target_names)
# plt.xlabel('true label')
# plt.ylabel('predicted label')
# plt.show()