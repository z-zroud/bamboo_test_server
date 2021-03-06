
class Response():
    def __init__(self, data={}, code=0, msg="Success"):
        self.code = code
        self.msg = msg
        self.data = data

    
    def to_dict(self):
        data = {'code': self.code, 'msg': self.msg}
        if self.data:
            data['data'] = self.data
        return data
