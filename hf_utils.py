# from transformers import pipeline

# classifier = pipeline(
#     "zero-shot-classification",
#     model="facebook/bart-large-mnli"
# )

# def classify_resume(text: str):

#     labels = [
#         "Backend Developer",
#         "Frontend Developer",
#         "Data Scientist",
#         "Machine Learning Engineer",
#         "DevOps Engineer",
#         "Mobile Developer"
#     ]

#     result = classifier(
#         text,
#         candidate_labels=labels
#     )

#     return {
#         "role": result["labels"][0],
#         "score": round(result["scores"][0] * 100, 2)
#     }