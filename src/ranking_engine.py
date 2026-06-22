from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def rank_candidates(jd_embedding, candidate_embeddings, candidates_df):

    scores = []

    for idx, embedding in enumerate(candidate_embeddings):
        similarity = cosine_similarity(
            [jd_embedding],
            [embedding]
        )[0][0]

        scores.append(similarity)

    candidates_df["Score"] = scores

    ranked = candidates_df.sort_values(
        by="Score",
        ascending=False
    )

    return ranked
