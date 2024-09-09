import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

def send_email():
    # Email content
    from_address = "kartik@project-lithium.com"
    to_address = "rakesh@project-lithium.com"
    subject = "Daily Vehicle & Sp Utilization Report"
    report_link = "https://prod-apnortheast-a.online.tableau.com/#/site/lithiumurbantech/views/Utilization_Report_VehicleAndSP/Home?:iid=3"

    # Calculate the date two days ago
    report_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

    # Create the HTML body with a clickable link
    body = f"""
    <html>
    <body>
        <p>Hello,</p>
        <p>This is the daily Vehicle & SP utilization Report for {report_date}.</p>
        <p>Please view the report <a href="{report_link}">here</a>.</p>
    <p>Thanks & Regards,</p>
    <p>Kartik Pandey</p>
    </body>
    </html>
    """

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the HTML body
    msg.attach(MIMEText(body, 'html'))

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, 'lpolrrwyvnffyynv')  # Use app password if needed for Gmail

    # Send the email
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

if __name__ == "__main__":
    send_email()
