# def authenticated(fn):
#     def wrapper(user: dict):
#         if user.get("valid"):
#             fn(user)

#     return wrapper


user1 = {"Lucas": 18}


def authenticated(send_text):
    def wrap_func(user):
        if user1["Lucas"] >= 18:
            return send_text(user1)
        else:
            print("The user is not old enough")
