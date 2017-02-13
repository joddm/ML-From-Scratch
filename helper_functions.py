from __future__ import division
import numpy as np
import math

# Split the data into train and test sets
def train_test_split(X, Y, test_size=0.5, shuffle=True):
	if shuffle:
		# Concatenate x and y and do a random shuffle
		x_y = np.concatenate((X,Y.reshape((1,len(Y))).T), axis=1)
		np.random.shuffle(x_y)
		X = x_y[:,:-1] # every column except the last
		Y = x_y[:,-1].astype(int) # last column
	# Split the training data from test data in the ratio specified in test_size
	split_i = len(Y) - int(len(Y)//(1/test_size))
	x_train, x_test = X[:split_i], X[split_i:]
	y_train, y_test = Y[:split_i], Y[split_i:]

	return x_train, x_test, y_train, y_test

def normalize(X, axis=-1, order=2):
	l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
	l2[l2==0] = 1
	return X / np.expand_dims(l2, axis)

# Return the variance of the features in dataset X
def calculate_variance(X):
	mean_matrix = np.ones(np.shape(X))*X.mean(0)
	n_features = len(X[0])
	variance = (1/n_features) * np.diag((X - mean_matrix).T.dot(X - mean_matrix))

	return variance

# Calculate the standard deviations of the features in dataset X
def calculate_std_dev(X):
	std_dev = np.sqrt(calculate_variance(X))

	return std_dev

# Making an array of nominal values into a binarized matrix
def categorical_to_binary(x):
	n_col = np.amax(x)+1
	binarized = np.zeros((len(x), n_col))
	for i in range(len(x)):
		binarized[i, x[i]] = 1

	return binarized

# Calculate the distance between two vectors
def euclidean_distance(x1, x2):
	distance = 0
	for i in range(len(x1)):
		distance += pow((x1[i] - x2[i]), 2)

	return math.sqrt(distance)

# Makes a row vector into an diagonal matrix
def make_diagonal(x):
	m = np.zeros((len(x), len(x)))
	for i in range(len(m[0])):
		m[i,i] = x[i]

	return m

# Compare y_true to y_pred and return the accuracy
def accuracy_score(y_true, y_pred):
	correct = 0
	for i in range(len(y_true)):
		eq = np.equal(y_true[i], y_pred[i])
		if isinstance(eq, np.bool_):
			if eq == False:
				continue
		elif False in eq:
			continue
		correct += 1

	return correct / len(y_true)

# Calculate the covariance matrix for the dataset X
def calculate_covariance_matrix(X, Y):
	X_mean = np.ones(np.shape(X))*X.mean(0)
	Y_mean = np.ones(np.shape(Y))*Y.mean(0)
	n_features = len(X[0])
	covariance_matrix = (1/n_features) * (X - X_mean).T.dot(Y - Y_mean)

	return covariance_matrix

# Calculate the correlation matrix for the dataset X
def calculate_correlation_matrix(X):
	covariance = calculate_covariance_matrix(X, X)
	n_features = len(covariance[0])
	std_dev = np.expand_dims(calculate_std_dev(X), 1)
	correlation = np.divide(covariance, std_dev.dot(std_dev.T))

	return correlation


