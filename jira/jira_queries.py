from jira.jira_client import JiraClient


class JiraQueries:

    @staticmethod
    def get_all_tickets():
        JiraClient.connect()

        return JiraClient.get_tickets()