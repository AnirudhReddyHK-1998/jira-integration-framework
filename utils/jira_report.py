import pandas as pd


from jira.jira_queries import JiraQueries


class JiraReport:

    @staticmethod
    def generate_report():

        tickets = JiraQueries.get_all_tickets()



        df = pd.DataFrame(tickets)
        df["priority"] = pd.Categorical(
            df["priority"],
            categories=["High", "Medium", "Low"],
            ordered=True
        )
        sorted_df = df.sort_values(
            by="priority"
        )

        print(sorted_df)

        return sorted_df