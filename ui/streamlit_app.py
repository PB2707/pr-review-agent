import streamlit as st
import requests
from pathlib import Path
st.set_page_config(
    page_title="AI PR Review Agent",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Pull Request Review Agent")

st.markdown(
    "Paste a **GitHub Pull Request URL** below to generate an AI-powered review."
)

pr_url = st.text_input(
    "GitHub PR URL",
    placeholder="https://github.com/owner/repo/pull/123"
)

review_button = st.button("🚀 Review Pull Request")

if review_button:

    if not pr_url:
        st.warning("Please enter a GitHub Pull Request URL.")
    else:

        with st.spinner("Reviewing Pull Request..."):

            response = requests.post(
                "http://127.0.0.1:8000/review",
                json={
                    "pr_url": pr_url
                },
            )

            if response.status_code == 200:
                review = response.json()
                

                st.success("Review completed successfully!")

                st.subheader("📋 Pull Request Information")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Author", review["author"])

                with col2:
                    st.metric("Files Reviewed", review["review_count"])

                st.write(f"**Title:** {review['title']}")
                st.write(f"**Execution Time:** {review['duration_seconds']} seconds")

                st.divider()

                for file in review["reviews"]:

                    st.header(f"📄 {file['filename']}")

                    risk = file["risk"]["level"]

                    if risk == "Low":
                        st.success(f"🟢 Risk Level: {risk}")
                    elif risk == "Medium":
                        st.warning(f"🟡 Risk Level: {risk}")
                    else:
                        st.error(f"🔴 Risk Level: {risk}")

                    st.subheader("Executive Summary")
                    st.write(file["summary"])

                    for agent in file["reviews"]:

                        with st.expander(f"{agent['agent']} Agent"):

                            st.write(agent["review"])

                    report_path = review.get("report_path")
                    # report_path = review.get("report_path")

                    st.write(report_path)

                    report_file = Path(report_path)

                    st.write(report_file.exists())

                    if report_path:

                        report_file = Path(report_path)

                        if report_file.exists():

                            with open(report_file, "rb") as f:
                                st.download_button(
                                    label="📥 Download Markdown Report",
                                    data=f,
                                    file_name=report_file.name,
                                    mime="text/markdown",
                                )

            else:
                st.error(response.text)