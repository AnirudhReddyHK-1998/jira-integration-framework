from jira.jira_queries import JiraQueries

tickets = JiraQueries.get_all_tickets()

for ticket in tickets:
    print(ticket)