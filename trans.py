from transformers import pipeline

generator = pipeline('text-generation', model='Alibaba-NLP/Tongyi-DeepResearch-30B-A3B')

data = input("Talk to me: ")
result = generator(data, num_return_sequences=1)

print(result[0]['generated_text'])