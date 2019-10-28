import os

RECEIVER = "christian@fableplus.com"

SMTP_USER = "no-reply@fableplus.com"
SMTP_PASSWORD = "gGNDUY5Vjsxqyaog"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_STARTTLS = os.environ.get("SMTP_STARTTLS", "true").lower() == "true"
