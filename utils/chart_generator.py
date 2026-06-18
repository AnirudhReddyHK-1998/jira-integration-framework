import matplotlib.pyplot as plt
import os


class ChartGenerator:

    @staticmethod
    def generate_chart(productivity):

        # Create reports folder
        os.makedirs(
            "reports",
            exist_ok=True
        )

        # Names and values
        names = list(
            productivity.keys()
        )

        tickets = list(
            productivity.values()
        )

        # Create figure
        plt.figure(
            figsize=(12, 6)
        )

        # Create bars
        bars = plt.bar(
            names,
            tickets
        )

        # Title
        plt.title(
            "Team Productivity Dashboard",
            fontsize=18,
            fontweight="bold"
        )

        # Labels
        plt.xlabel(
            "Team Members"
        )

        plt.ylabel(
            "Tickets Closed"
        )

        # Grid
        plt.grid(
            axis="y",
            linestyle="--",
            alpha=0.5
        )

        # Add values on bars
        for bar in bars:

            height = bar.get_height()

            plt.text(
                bar.get_x() +
                bar.get_width() / 2,

                height + 0.05,

                str(height),

                ha="center"
            )

        # Layout
        plt.tight_layout()

        # Save chart
        plt.savefig(
            "reports/team_productivity.png"
        )

        # Close figure
        plt.close()

        print(
            "Chart generated successfully"
        )