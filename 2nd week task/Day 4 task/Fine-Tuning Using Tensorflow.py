from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf

# Load tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Sample data
texts = ["Amazing experience", "Worst product ever"]
labels = tf.constant([1, 0])

# Tokenization
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='tf')

# Compile model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=2e-5),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train
model.fit(inputs.data, labels, epochs=2)
