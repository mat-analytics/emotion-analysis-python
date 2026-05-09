from transformers import pipeline

# Downloading and loading ready model to analyze emotions of given text
analyzer = pipeline("sentiment-analysis")


# Input your text and it will be judged - positive/negative
text_to_analyze = input("Type your text: ")
result = analyzer(text_to_analyze)

print(f"Text: {text_to_analyze}")
print(f"AI analysis: {result}")