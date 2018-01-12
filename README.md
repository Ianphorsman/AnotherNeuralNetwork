# AnotherNeuralNetwork

data recipes contain jupyter notebooks

X, y = make_moons(1000, noise=0.4, random_state=333)
X_train, X_test, y_train, y_test = train_test_split(X, y)

mlp = MLP(X_train, y_train, iterations=1500, learning_rate=0.003)

mlp.train(mlp.X, mlp.y)

print(mlp.test_accuracy(X_test, np.atleast_2d(y_test)))

mlp.plot_decision_boundary(X_test[:, 0], X_test[:, 1], y_test)
mlp.plot_performance()