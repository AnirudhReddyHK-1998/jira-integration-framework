import pyautogui
import time
import os


class DashboardCapture:

    @staticmethod
    def capture_dashboard():

        # Wait for dashboard to load
        time.sleep(5)

        # Create reports folder
        os.makedirs(
            "reports",
            exist_ok=True
        )

        # Take screenshot
        screenshot = pyautogui.screenshot()

        # Save screenshot
        screenshot.save(
            "reports/dashboard_screenshot.png"
        )

        print(
            "Dashboard screenshot captured"
        )