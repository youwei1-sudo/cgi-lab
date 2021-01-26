#!/usr/bin/env python3
import os
import json
import sys

# This CGI script

# print('Content-Type: text/html')
# print('Content-Type: application/octent-stream')
# print('Content-Type: application/json')
# # seperate header and content, q1
# print()
# # check in web, we use json 
# print(json.dumps(dict(os.environ), indent=2))

# #####Q3
# ? how to add more parameters &
# print('Content-Type: text/html')
# # seperate header and content
# print()
# print("""<!DOCTYPE html>	
# <html>
# <body>
# <h1>HELLO I AM HTML</h1>
# """)
# print("<ul>")
# print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
# for parameter in os.environ['QUERY_STRING'].split('&'):
# 	(name, value) = parameter.split('=')
# 	print(f"<li><em>{name} </em> = {value} </li>")
# print("""
# </ul>
# """)
# print("""
# </ul>
# </body>
# </html>
# # """)






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
	# print('Content-Type: text/html')
	
	# seperate header and content
	print()

	print(login_page())

	# login_page()

if __name__ == '__main__':

	main()
