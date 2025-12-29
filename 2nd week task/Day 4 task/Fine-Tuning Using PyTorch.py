from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
import torch

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Sample input
texts = ["I love this movie", "This movie is bad"]
labels = torch.tensor([1, 0])

# Tokenization
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# Forward pass
outputs = model(**inputs, labels=labels)
loss = outputs.loss

# Backpropagation
loss.backward()
