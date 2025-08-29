from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Minibot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self.questions = [item["question"] for item in self.knowledge_base]
        
        print("Encoding knowledge base questions...")
        self.question_embeddings = self.model.encode(self.questions)
        print("Encoding complete.")

    def get_answer(self, user_query):
        query_embedding = self.model.encode([user_query])

        similarities = cosine_similarity(query_embedding, self.question_embeddings)

        most_similar_idx = np.argmax(similarities)
        max_similarity = similarities[0][most_similar_idx]

        similarity_threshold = 0.5
        
        if max_similarity > similarity_threshold:
            return self.knowledge_base[most_similar_idx]["answer"]
        else:
            return "I'm sorry, I don't have an answer to that in my knowledge base."
