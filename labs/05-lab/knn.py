from sklearn import datasets
from sklearn.metrics import euclidean_distances
from sklearn.model_selection import train_test_split

class KNN:

    def __init__(self, k, X_train, y_train):
        self.k = k
        self.X_train = X_train
        self.y_train = y_train
        self.distance_matrix = []

    def euclidean_dist(self, x, y):
        res = 0
        for i in range(len(x)):
            res += (x[i] - y[i])**2
        return res**(1/2)

    def train(self):
        for vector1 in self.X_train:
            for vector2 in self.X_train:
                 self.distance_matrix.append(self.euclidean_dist(vector1, vector2))
        

    def predict(self, example):
        return ...

    def get_error(self, predicted, actual):
        return sum(map(lambda x : 1 if (x[0] != x[1]) else 0, zip(predicted, actual))) / len(predicted)

    def test(self, test_input, labels):
        actual = labels
        predicted = (self.predict(test_input))
        print("error = ", self.get_error(predicted, actual))

# Add the dataset here
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

# Split the data 70:30 and predict.
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, test_size=0.3, random_state=1)

# create a new object of class KNN
knn = KNN(3, Xtrain, ytrain)
knn.train()

# plot a boxplot that is grouped by Species. 
# You may have to ignore the ID column

# predict the labels using KNN

# use the test function to compute the error
