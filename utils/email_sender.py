import win32com.client
import os


class EmailSender:

    @staticmethod
    def send_email(
            receiver_email,
            report_file,
            chart_file
    ):
        try:
            print("Opening Outlook")

            # Open Outlook
            outlook = win32com.client.Dispatch(
                "Outlook.Application"
            )

            # Create email
            mail = outlook.CreateItem(0)

            mail.To = receiver_email

            mail.Subject = (
                "Automated Standup Metrics Report"
            )

            mail.Body = """
Hello Team,

Please find attached today's productivity report.

Dashboard Link:
https://jira-integration-framework-5evqdmpazr3kumbh8uqjgq.streamlit.app/
Regards,
Automation Framework
"""

            # Attach files
            mail.Attachments.Add(
                os.path.abspath(report_file)
            )

            mail.Attachments.Add(
                os.path.abspath(chart_file)
            )

            # Send email automatically
            mail.Send()

            print("Email sent successfully")

        except Exception as e:
            print(
                f"Failed to send email: {e}"
            )