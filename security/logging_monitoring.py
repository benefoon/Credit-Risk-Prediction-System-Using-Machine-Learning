import logging

logging.basicConfig(
    filename="security.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.WARNING
)

def log_suspicious_activity(user, activity):
    """Log potential security threats"""
    logging.warning(f"Suspicious Activity - User: {user}, Activity: {activity}")

# Example Usage
log_suspicious_activity("user123", "Failed login attempt 5 times")
