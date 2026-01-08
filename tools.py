"""
Tools module containing all function tools for the sales agent system.
Includes email sending functionality and other utilities.
"""

import os
from typing import Dict
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from agents import function_tool
from config import Config


@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """
    Send out an email with the given subject and HTML body to all sales prospects.

    Args:
        subject: The email subject line
        html_body: The HTML formatted email body

    Returns:
        Dict containing the status of the email send operation
    """
    sg = sendgrid.SendGridAPIClient(api_key=Config.SENDGRID_API_KEY)
    from_email = Email(Config.EMAIL_FROM)
    to_email = To(Config.EMAIL_TO)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}
