import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path("index.html").read_text())


# def read_text(self, encoding=None, errors=None):
#     """
#     Open the file in text mode, read it, and close the file.
#     """
#     encoding = io.text_encoding(encoding)
#     with self.open(mode="r", encoding=encoding, errors=errors) as f:
#         return f.read()


email = EmailMessage()
email["from"] = "Pythonclass"
email["to"] = "tico41st@hotmail.com"
email["subject"] = "You won 1,000,000 dollars!"
email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("pydevhc@gmail.com", "Aig2024$")
    smtp.send_message(email)
print("all good boss!")


# import smtplib as smtp

# connection = smtp.SMTP_SSL("smtp.gmail.com", 465)

# email_addr = "pydevhc@gmail.com"
# email_passwd = "obpivkegkoerecoa"
# connection.login(email_addr, email_passwd)
# connection.sendmail(
#     from_addr=email_addr,
#     to_addrs="recipient@something.com",
#     msg="Sent from my IDE. Hehe",
# )
# connection.close()


# self.user, self.password = user, password
#         for authmethod in authlist:
#             method_name = 'auth_' + authmethod.lower().replace('-', '_')
#             try:
#                 (code, resp) = self.auth(
#                     authmethod, getattr(self, method_name),
#                     initial_response_ok=initial_response_ok)
#                 # 235 == 'Authentication successful'
#                 # 503 == 'Error: already authenticated'
#                 if code in (235, 503):
#                     return (code, resp)
#             except SMTPAuthenticationError as e:
#                 last_exception = e

#         # We could not login successfully.  Return result of last attempt.
#         raise last_exception
