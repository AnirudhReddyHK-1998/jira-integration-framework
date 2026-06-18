import pandas as pd

from utils.logger import logger
from utils.email_sender import EmailSender
from utils.dashboard_capture import DashboardCapture
from config.config import RECEIVER_EMAIL
from utils.folder_helper import FolderHelper
from utils.jira_report import JiraReport
from utils.chart_generator import ChartGenerator


def main():
    try:
        # Create required folders
        FolderHelper.create_folders()

        logger.info("Starting Jira Report Automation")

        # Get Jira data
        df = JiraReport.generate_report()

        if df is None or df.empty:
            logger.error("No Jira data found")
            return

        # Save Jira data to Excel
        report_path = "reports/jira_report.xlsx"

        with pd.ExcelWriter(
            report_path,
            engine="openpyxl"
        ) as writer:
            df.to_excel(
                writer,
                sheet_name="Jira Report",
                index=False
            )

        logger.info("Jira Excel report generated")

        # Generate Priority Chart
        chart_data = (
            df["priority"]
            .value_counts()
            .to_dict()
        )

        chart_path = "reports/team_productivity.png"

        ChartGenerator.generate_chart(
            chart_data
        )

        logger.info("Chart generated successfully")

        # Capture dashboard screenshot
        DashboardCapture.capture_dashboard()

        logger.info("Dashboard captured successfully")

        # Send email
        print("Calling email function")

        EmailSender.send_email(
            RECEIVER_EMAIL,
            report_path,
            chart_path
        )

        logger.info(
            "Jira automation completed successfully"
        )

    except Exception as e:
        logger.error(
            f"Framework execution failed: {e}"
        )


if __name__ == "__main__":
    main()