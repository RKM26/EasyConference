"""
all routes
"""

from controllers import *

routes = [
        (r'/audio_stream', main.AudioStreamHandler),
        (r'/upload', main.AudioUploadHandler),
        (r'/test', main.TestHandler)
    ]