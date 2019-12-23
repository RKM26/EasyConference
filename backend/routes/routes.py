"""
all routes
"""

from controllers import *

routes = [
        (r'/audio_stream', main.AudioStreamHandler),
    ]