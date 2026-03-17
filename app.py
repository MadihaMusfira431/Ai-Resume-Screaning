import streamlit as st
import pandas as pd

st.title("AI Resume Screening System")

# Load dataset
df = pd.read_csv("resume.csv")

st.subheader("Resume Dataset")
st.dataframe(df)

# Input job skills
job_skills = st.text_input("Enter required skills (comma separated)")

if st.button("Find Best Candidates"):

    if job_skills == "":
        st.warning("Please enter required skills")
    else:
        required = [x.strip().lower() for x in job_skills.split(",")]

        scores = []

        for index, row in df.iterrows():
            candidate_skills = [s.strip().lower() for s in row["Skills"].split(",")]
            match = len(set(required) & set(candidate_skills))
            scores.append(match)

        df["MatchScore"] = scores

        ranked = df.sort_values(by="MatchScore", ascending=False)

        st.subheader("Top Candidates")
        st.dataframe(ranked)

        # download result
        st.download_button(
            "Download Results",
            ranked.to_csv(index=False),
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )