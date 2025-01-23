# script 1
resp = request.put("url_here", headers=headers, json=payload)

# script 2
# Imports
import requests
from scratchsession import prepare_session
# Make a new `requests.Session` object
session = prepare_session('username', 'pass')
# Set up python dict
payload = {"A python":"dictionary of scratch data"}
# Put the data
session.put("https://projects.scratch.mit.edu/716989190", json=payload)
