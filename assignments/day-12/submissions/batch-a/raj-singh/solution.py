from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
# Question 1

# Supervised Learning
print("Supervised Learning: Learns from labeled data where correct answers are already known.")

# Unsupervised Learning
print("Unsupervised Learning: Learns patterns and groups from unlabeled data.")

# Reinforcement Learning
print("Reinforcement Learning: Learns by receiving rewards and penalties from the environment.")


# Question 2

print("\nQuestion 2")

# House price prediction
print("1. House Price Prediction -> Supervised Learning")

# Customer grouping
print("2. Customer Grouping -> Unsupervised Learning")

# Spam detection
print("3. Spam Detection -> Supervised Learning")

# News article grouping
print("4. News Article Grouping -> Unsupervised Learning")


# Question 3

print("\nQuestion 3")

# Temperature prediction
print("1. Tomorrow Temperature -> Regression")

# Pass or fail prediction
print("2. Student Pass or Fail -> Classification")

# Bike price prediction
print("3. Second-hand Bike Price -> Regression")

# Cat or dog prediction
print("4. Cat or Dog Image -> Classification")


# Question 4

print("\nQuestion 4")

print("Learning Type: Supervised Learning")
print("Problem Type: Classification")
print(
    "Explanation: Loan data contains labels "
    "(approved/rejected), therefore it is supervised learning "
    "and classification."
)
# [Income, Credit Score, Age, Employment Type, Previous Loan History]
X_train = [
    [50000, 750, 25, 1, 1],
    [30000, 650, 22, 0, 0],
    [70000, 800, 35, 1, 1],
    [25000, 600, 21, 0, 0],
]

y_train = [1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

prediction = model.predict([[55000, 720, 28, 1, 1]])

print("Loan Prediction:", "Approved" if prediction[0] == 1 else "Rejected")


# Question 5


print("\nQuestion 5")

print("Learning Type: Unsupervised Learning")
print("Problem Type: Clustering")
print(
    "Explanation: Labels such as premium or regular are not provided, "
    "so the algorithm discovers groups automatically."
)


#customer age,total purchases, application usage time
customers = [
    [20, 5000, 30],
    [22, 5500, 35],
    [45, 25000, 120],
    [48, 28000, 130]
]

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(customers)

print("Customer Groups:", kmeans.labels_)


# Question 6

print("\nQuestion 6")

print(
    "A robot receives a reward for correct movement and a penalty "
    "for falling, so it learns by trial and error. "
    "This is Reinforcement Learning."
)


# Question 7


print("\nQuestion 7")

print(
    "fit(): Like studying before an exam. "
    "The model learns patterns from training data."
)

print(
    "predict(): Like writing the exam. "
    "The model uses learned knowledge to answer new questions."
)

# Question 8

print("\nQuestion 8")

print("Model A -> Underfit")
print("Model B -> Right Fit")
print("Model C -> Overfit")