
import pandas as pd

def load_candidates(file_path):
    candidates = pd.read_csv(file_path)
    return candidates

def load_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        jd = file.read()
    return jd
