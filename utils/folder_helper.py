import os


class FolderHelper:

    @staticmethod
    def create_folders():

        folders = [
            "output",
            "reports",
            "logs"
        ]

        for folder in folders:

            os.makedirs(
                folder,
                exist_ok=True
            )