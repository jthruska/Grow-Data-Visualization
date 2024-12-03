
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to create a word cloud
def wordCloud(df, column, ignore):
    # Variables to store the words and the end of the words
    words = ''
    stopwords = set(STOPWORDS)

    # iterating through each word in the given column of the csv file
    for val in df.get(column):
        # Convert each value into a string
        val = str(val)
        tokens = val.split() # splitting the string

        # Converting each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        # Only add the word if its longer than 1 letter and isn't in the ignored words
        if (not len(tokens) == 1) and ignore.count(tokens) == 0:
            words += " ".join(tokens) + " "  # adding the tokens to the words

    # Removing the ignored words
    for word in ignore:
        words = words.replace(word, " ", words.count(word))

    # Replacing words with other words also in the word cloud with the same meaning
    words = words.replace("help ", "helpful ", words.count("help"))
    words = words.replace("customization ", "customize ", words.count("help"))
    words = words.replace("achieved ", "achieving ", words.count("help"))

    # Creating the word cloud
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(words)

    # plotting the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


# Reading the questionnaire csv
pre = pd.read_csv('Grow Pre-Test Questionnaire.csv')
post = pd.read_csv('Grow Post-Test Questionnaire.csv')
test = pd.read_csv('Task Times.csv')

# Converting columns stored as strings to ints
for column in ["What is your current relationship with social media like?","I would like to improve my relationship with social media.","What is your opinion on self-help apps?","How likely are you to use a self-help app?"]:
    np.floor(pd.to_numeric(pre[column], errors='coerce')).astype(pd.Int64Dtype())
for column in ["How easy was it to open an article?","How easy was it to view all of your plants?","How easy was it to view your friend’s plants?","How easy was it to create a goal that repeats?","How easy was it to see how many times snap chat has been opened today?","How easy was it to buy a new color for your plant’s pot?","How easy was it to customize your plant?","Rate this app from 1-5 stars.","How usable do you think this app is?"]:
    np.floor(pd.to_numeric(post[column], errors='coerce')).astype(pd.Int64Dtype())


# Creating word clouds of the free response questions
wordCloud(pre, "Considering the name \"Grow\" and the app's purpose, what are some first-impressions you have about it?", ["app", "game", "grow", "become", "used", "name", "sounds", "people", "better"])
wordCloud(post, "What is one part of the app that you enjoyed? Why did you enjoy it?", ["enjoyed", "grow", "part", "enjoyable", "liked", "really", "know", "appling", "pretend", "people", "someone", "something", "see", " ing ", " s ", "'s"])
wordCloud(post, "What was the hardest part of the app for you to use? Why was it tough for you?", ["took", "hardest", "thought", "page", "front", "think", "make", "maybe", "challenging", "app", "instead", "metaphor", "usually", "know", "based", "pertaining", " non", "want", "easy", "way", "may", "main", "every", "people", "tell", "things", "figure"])
wordCloud(post, "What is one part of the app that you think could be improved? How would you improve it?", ["something", "app", "met", "think", "grow", "quite", "good", "including", "area", "one", "e.g.", " s ", "wizard", "certain", "weird", "kind", "because", "use", "thing", "based", "already", "never", "failed", "way", "know", "come", "difficult", "maybe", "figure", "people", "concerned", "philosophically", "another", "similar", "found", "felt", "wether", "whether", "called", "neither", "needing", "whether"," s ", " al "])


# Creating a bar graphs with standard deviation
# Ease of use stats
easeCols = ["How easy was it to open an article?","How easy was it to view all of your plants?","How easy was it to view your friend’s plants?","How easy was it to create a goal that repeats?","How easy was it to see how many times snap chat has been opened today?","How easy was it to buy a new color for your plant’s pot?","How easy was it to customize your plant?"]

# Finding the mean and standard deviation for the columns
mean = post[easeCols].mean()
std = post[easeCols].std()

# Plotting the bars and standard deviation
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(easeCols) + 1), mean, color='green', alpha=0.7)
plt.errorbar(range(1, len(easeCols) + 1), mean, std, fmt="k_", linewidth=2, capsize=30, ecolor='black')

# Labeling the axes, giving the chart a name, and showing the chart
plt.xlabel("Tasks")
plt.ylabel("Ease of Use Rating")
plt.title("Task Ease of Use Mean with Standard Deviation")
plt.show()


# Star ratings
# Bar graph with standard deviation
rating = "Rate this app from 1-5 stars."

# Finding the mean and standard deviation for the ratings
mean = post[rating].mean()
std = post[rating].std()

# Plotting the bars and standard deviation
plt.figure(figsize=(4, 6))
plt.bar("User Ratings", mean, color='orange', alpha=0.7)
plt.errorbar("User Ratings", mean, std, fmt="k_", linewidth=2, capsize=30, ecolor='black')

# Labeling the axes, giving the chart a name, and showing the chart
plt.ylabel("Rating out of 5 stars")
plt.title("User Ratings Mean with Standard Deviation")
plt.show()


# Creating a bar graphs with standard deviation
# Task times
tasks = ["Task " + str(i) for i in range(1, 8)]

# Finding the mean and standard deviation for the columns
mean = test[tasks].mean()
std = test[tasks].std()

# Plotting the bars and standard deviation
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(tasks) + 1), mean, color='darkblue', alpha=0.7)
plt.errorbar(range(1, len(tasks) + 1), mean, std, fmt="k_", linewidth=2, capsize=30, ecolor='black')

# Labeling the axes, giving the chart a name, and showing the chart
plt.xlabel("Tasks")
plt.ylabel("Time in Seconds")
plt.title("Task Time Means with Standard Deviation")
plt.show()


# Scatter Plot
colors = np.array(range(0,350,10))
check = plt.scatter(post[easeCols], test[tasks], c=colors, cmap='viridis')
plt.show()