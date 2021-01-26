#!/usr/bin/env python3
import os
import json
import sys
from templates import secret_page
import secret 
# This CGI script





def login_page():
    """
    Returns the HTML for the login page.
    """
    return _wrapper(r"""
    <!DOCTYPE html>	
	<html>
	<body>
    <h1> Welcome! </h1>

    <form method="POST" action="login.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    </body>
    </html>
    """)

def _wrapper(page):
    """
    Wraps some text in common HTML.
    """
    return ("""
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 24em;
                margin: auto;
                color: #333;
                background-color: #fdfdfd
            }

            .spoilers {
                color: rgba(0,0,0,0); border-bottom: 1px dashed #ccc
            }
            .spoilers:hover {
                transition: color 250ms;
                color: rgba(36, 36, 36, 1)
            }

            label {
                display: flex;
                flex-direction: row;
            }

            label > span {
                flex: 0;
            }

            label> input {
                flex: 1;
            }

            button {
                font-size: larger;
                float: right;
                margin-top: 6px;
            }
        </style>
    </head>
    <body>
    """ + page + """
    </body>
    </html>
    """)

def main():
	tuple_array = []

	# print('Content-Type: text/html')
	
	# seperate header and content
	print()

	
	# # q 6
	cookie_tuple_array = []
	# q 6
	client_cookie  = os.environ.get("HTTP_COOKIE", 0)
	# client_cookie.split(';')
	secrete_flag =False

	if (client_cookie != "") :
		for parameter in client_cookie.split(';'):
			(name, value) = parameter.strip().split('=')
			cookie_tuple_array.append((name,value))
		# if (cookie_tuple_array[0][0] == os.environ.get("GNOME_DESKTOP_SESSION_ID", 0) ):
		for t in cookie_tuple_array:
			if (t[0] == "session_id"):
				secrete_flag = True
	else :
		# print(login_page())
		pass
	if (secrete_flag ) :
		print(login_page())
	else:
		print(secret_page(secret.username, secret.password))

if __name__ == '__main__':

	main()
