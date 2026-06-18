class DataProcessor:

    @staticmethod
    def generate_summary(df):

        summary = (
            df.groupby(
                ["Assigned To", "Status"]
            )
            .size()
            .unstack(fill_value=0)
        )

        productivity = (
            df.groupby("Assigned To")[
                ["Bugs Raised", "Test Cases"]
            ]
            .sum()
        )

        return summary, productivity