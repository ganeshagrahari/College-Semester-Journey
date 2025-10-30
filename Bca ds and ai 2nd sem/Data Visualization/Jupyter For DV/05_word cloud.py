<<<<<<< HEAD
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = "Data visualization with word clouds is a great way to highlight the most frequent words in a dataset. Word clouds are visually appealing and easy to interpret."

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()
=======
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = "Data visualization with word clouds is a great way to highlight the most frequent words in a dataset. Word clouds are visually appealing and easy to interpret."

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()
>>>>>>> dc4cba81a1c391062d7063dbe308d4162a8a9149
