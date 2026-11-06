
from pathlib import Path
import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

file_path = Path(__file__).parent / "original.txt"
with open(file_path, "r", encoding="utf-8") as file:
    original_text = file.read()

with open(Path(__file__).parent / "twilight.txt", "r", encoding="utf-8") as file:
    twilight_text = file.read()

with open(Path(__file__).parent / "botw.txt", "r", encoding="utf-8") as file:
    botw_text = file.read()

print("Total characters:", len(original_text))
print("Total words:", len(original_text.split()))
print("\nFirst 300 characters:")
print(original_text[:300])

model = markovify.Text(original_text, state_size=2)

synthetic_sentences = []
for i in range(10):
    sentence = model.make_sentence(tries=100)
    if sentence:
        synthetic_sentences.append(sentence)

synthetic_text = " ".join(synthetic_sentences)

print("\n=== SYNTHETIC TEXT ===")
print(synthetic_text)

with open("synthetic.txt", "w", encoding="utf-8") as file:
    file.write(synthetic_text)

print("\nSynthetic text saved successfully!")
print("Generated words:", len(synthetic_text.split()))

texts = [original_text, synthetic_text, twilight_text, botw_text]

vectorizer = TfidfVectorizer(stop_words="english")

tfidf_matrix = vectorizer.fit_transform(texts)

print("\nTF-IDF")
print("Matrix shape:", tfidf_matrix.shape)
print("Vocabulary size:", len(vectorizer.vocabulary_))

similarities = cosine_similarity(
    tfidf_matrix[1:2],
    tfidf_matrix[[0, 2, 3]]
)[0]

print("\nCOSINE SIMILARITY:")
print(f"Ocarina of Time: {similarities[0] * 100:.2f}%")
print(f"Twilight Princess: {similarities[1] * 100:.2f}%")
print(f"Breath of the Wild: {similarities[2] * 100:.2f}%")
