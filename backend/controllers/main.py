from controllers.modules import *


__UPLOADS__ = "uploads/"


class AudioStreamHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    @coroutine
    def get(self):
        self.write(json.dumps({
            "status": "status",
            "message": "message",
        }))

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        json_data = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(json_data))

    def options(self):
        self.set_status(204)
        self.finish()


class AudioUploadHandler(RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        # self.set_header("Content-Type", "application/json")
        # self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header('Access-Control-Allow-Methods', 'GET, OPTIONS')

    @coroutine
    def post(self):
        fileinfo = self.request.files['file'][0]
        print("fileinfo is", fileinfo)
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(__UPLOADS__ + cname, 'w')
        fh.write(fileinfo['body'])
        self.finish(cname + " is uploaded!! Check %s folder" %__UPLOADS__)

    def write_error(self, status_code, message="Internal Server Error", **kwargs):
        json_data = {
            'status': int(status_code),
            'message': message
        }
        self.write(json.dumps(json_data))

    def options(self):
        self.set_status(204)
        self.finish()


class TestHandler(RequestHandler):
    def get(self):
        self.write("Rishab chutiya h\n")