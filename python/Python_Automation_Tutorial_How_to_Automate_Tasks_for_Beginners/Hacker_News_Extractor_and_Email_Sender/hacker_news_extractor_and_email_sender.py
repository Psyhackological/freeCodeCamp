import requests  # HTTP requests
from bs4 import BeautifulSoup  # Web Scraping
import smtplib  # Sending the email
from email.mime.multipart import MIMEMultipart  # Email-
from email.mime.text import MIMEText  # -Body
import datetime  # System date and time manipulation


# Extracting Hacker News Stories
def extract_news(url):
    print("Extracting Hacker News Stories...")  # Action message
    scrapped_content = ''  # Placeholder for extracted string manipulation
    content_header = f'<b>HN Top Stories:</b>\n<br>{"-" * 50}<br>'  # Header for the email
    scrapped_content += content_header  # Concatenate email header with scrapped content
    response = requests.get(url)  # Let's get the requests of this URL, shall we?
    response_content = response.content  # Let's see its content
    soup = BeautifulSoup(response_content, 'html.parser')  # And make a soup of it to work with
    # Then make some counter with enumerate() with specific td element
    for i, tag in enumerate(soup.find_all("td", attrs={"class": "title", "valign": ''}), 1):
        scrapped_content += (f"{i}. {tag.text}\n<br>" if tag.text != "More" else '')  # Properly format it
    scrapped_content += f"{scrapped_content}<br>------<br><br><br>End of Message"
    return scrapped_content  # And after everything is done - return it


#  Composing Email Body
def compose_email_body(message, from_email, to_email, email_body):
    print("Composing Email...")  # Action message

    now = datetime.datetime.now()  # datetime object with current time

    message["Subject"] = f"Top News Stories HN [Automated E-mail]{now.day}-{now.month}-{now.year}"  # Subject of the Email
    message["From"] = from_email  # From whose account that should be sent
    message["To"] = to_email  # To whose account that should be sent

    message.attach(MIMEText(email_body, "html"))  # Hello object Message, this is my email_body, and it is in HTML


def initialize_and_send(message, from_email, to_email, server_address, port, password):
    print("Initializing Server....")  # Action message

    server = smtplib.SMTP(server_address, port)  # Initialize connection with SMTP server
    server.set_debuglevel(0)  # 0 - Do not see the error messages, 1 - See the error messages
    server.ehlo()  # Initialing server with ehlo
    server.starttls()  # Starting TLS connection
    server.login(from_email, password)  # Log in to server
    server.send_message(message.as_string(), from_email, to_email)  # Sending the e-mail
    server.quit()

    print("Email has been sent...")  # Confirmation message


def main():
    content = extract_news("https://news.ycombinator.com/")  # Email content

    from_email = ""  # Sender
    to_email = ""  # Receiver
    message = MIMEMultipart()

    server_address = ""  # SMTP Server Address
    port = 0  # Port Number
    password = ""  # Password of the sender

    compose_email_body(message, from_email, to_email, content)
    initialize_and_send(message, from_email, to_email, server_address, port, password)


if __name__ == "__main__":
    main()
