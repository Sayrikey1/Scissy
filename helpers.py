import random
import string

from functools import wraps
from flask import request, redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is logged in
        if session.get("user_id") is None:
            # Redirect to the login page if user is not logged in
            return redirect(url_for('login'))  # , next=request.url

        # Call the original function if user is logged in
        return f(*args, **kwargs)

    # Return the decorated function
    return decorated_function


def random_str(digit=7):
    char = ""
    for i in range(digit):
        chars += random.choice(string.ascii_letters + string.digits)
    return char


def validate_url(url):
    import re
    # Regular expression pattern for validating URLs
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # Matches http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # Matches localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Matches IP address
        r'(?::\d+)?'  # Matches optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return (re.match(regex, url) is not None)  # True
