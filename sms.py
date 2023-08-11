# Sending SMS using Python - using Twilio API

# from twilio.rest import Client

# account_sid = "AC612fc606e34f61dfbfa3beedcc1ecbef"
# auth_token = "c935d3e632f61a90843d9c2c97374be3"
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_="+15739953981", body="Wow we are on", to="+5511934375071"
# )

# print(message.sid)

import requests

requests.post(
    "https://ntfy.sh/mytopic", data="Backup successful 😀".encode(encoding="utf-8")
)

# import requests

# requests.post(
#     "https://ntfy.sh/mydoorbell",
#     data="""There's someone at the door. 🐶

# Please check if it's a good boy or a hooman.
# Doggies have been known to ring the doorbell.""".encode(
#         "utf-8"
#     ),
#     headers={
#         "Click": "https://home.nest.com/",
#         "Attach": "https://nest.com/view/yAxkasd.jpg",
#         "Actions": "http, Open door, https://api.nest.com/open/yAxkasd, clear=true",
#         "Email": "phil@example.com",
#     },
# )
