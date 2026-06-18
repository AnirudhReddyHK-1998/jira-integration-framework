import logging
import os

# Create logs folder automatically
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/framework.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()



# this code creates logs/framework.log

# and stores framework execution logs.