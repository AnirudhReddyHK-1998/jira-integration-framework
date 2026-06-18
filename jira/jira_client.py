from jira.jira_mock_data import MOCK_JIRA_TICKETS


class JiraClient:

    @staticmethod
    def connect():

        print(
            "Connected to Jira Mock Server"
        )

        return True

    @staticmethod
    def get_tickets():

        return MOCK_JIRA_TICKETS
