def generate_explanation(candidate):

    return (
        f"{candidate['Name']} ranked highly because of "
        f"strong skills in {candidate['Skills']} "
        f"and holds certification "
        f"{candidate['Certifications']}."
    )
