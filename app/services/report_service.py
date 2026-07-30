from pathlib import Path


class ReportService:

    def __init__(self):
        self.output_dir = Path("reports")
        self.output_dir.mkdir(exist_ok=True)

    def generate_markdown(self, review_result):

        filename = (
            review_result["title"]
            .replace(" ", "_")
            .replace("/", "_")
        )

        report_path = self.output_dir / f"{filename}_review.md"

        markdown = f"""# Pull Request Review

    ## PR Information

    **Title:** {review_result['title']}

    **Author:** {review_result['author']}

    **Files Reviewed:** {review_result['review_count']}

    **Execution Time:** {review_result['duration_seconds']} seconds

    ---
    """

        for file in review_result["reviews"]:

            markdown += f"""

    # {file['filename']}

    ## Executive Summary

    {file['summary']}

    ## Risk

    **Level:** {file['risk']['level']}

    **Score:** {file['risk']['score']}

    """

            for review in file["reviews"]:

                markdown += f"""
    ### {review['agent']} Agent

    {review['review']}

    """

        report_path.write_text(markdown)

        return str(report_path)

        