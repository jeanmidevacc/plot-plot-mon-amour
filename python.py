import matplotlib.pyplot as plt

fig,ax=plt.subplots(figsize=(12,6))# format of the image
plt.style.use('ggplot')
# do your magic around plot

plt.xlabel("Day") # Define the x axis
plt.ylabel("Count of items released")  # Define the y axis

ax.get_legend().remove() # Drop the legend
fig.tight_layout() # Extend the plot to the edges of the image
plt.show()
