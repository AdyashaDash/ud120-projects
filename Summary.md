# Naive Bayes
* Example of supervised vs. non-supervised learning applications
* Features and labels examples (notes, tempo, pitch -> features; like, dislike -> label)
* Bumpiness scatter plots -> choosing visually what fits
* Decision surfaces + what makes a surface good?
* Getting started with sklearn - Gaussian NB
* Accuracy, training and testing datasets
* Bayes Rule, cancer test example, prior and posterior
* Quizzes on normalization, total probabilities
* "Naive" Bayes, because e.g. it doesn't take into account word order
* Strength: easy, can handle big feature spaces
* Weakness: fails on phrases (when it comes to text prediction)
* Mini project: finding the author. Track accuracy

# Support Vector Machine
* "Finds a hyperplane that maximizes margin"
* What's a good "separating line" -> play around with margins
* Margin: distance to nearest point
* Kernel trick: make data linearly separable in a higher dimension -> e.g. data not separable in x and y, but separable in x^2 and y^2
* Parameters are used before creating your model, so before fitting
* Some important parameters: 
	* 'Kernel' itself (linear vs rbf)
	* 'C': tradeoff between smooth decision boundary vs. classifying training data correctly -> penalizes error
	* 'gamma': no effect on linear kernel; Otherwise, how far the influence of a single training example can reach -> low gamma = far, high gamma = weigh closeby points more heavily in finding separation line. Low gamma eventually makes decision boundary more linear and smooth as faraway points also contribute
* SVM vs. GNB:
	* SVM: complicated domain with clear marginal separation, but cubic in dataset size so slow for large datasets. Problem with overfitting.
	* GNB: lots of features, lots of noise, overlapping classes -> better to use in these cases
* Mini project: Author ID (accuracy, timing, playing with smaller training set, speed vs. accuracy tradeoff, RBF kernel + optimize C parameter)