
# File for remote file managing

class RemoteFile:
    def __init__(self, filename, mode='r', server_ip='127.0.0.1', port='4444'):
        self.__filename = filename
        self.__mode = mode
        self.__server_ip = server_ip
        self.__port = port
        self.__fp = None

    # Custom write method
    def remote_write(self, text:str):
        if self.__fp:
            print(f"Connection to server: {self.__server_ip}:{self.__port}")
            self.__fp.write(text)

    def __enter__(self):
        print("__enter__")
        self.__fp = open(self.__filename, mode=self.__mode)
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        print("__exit__")
        self.__fp.close()

    # <Open remote file 'server.log', mode 'wat 0x26d6c0bd220>
    def __repr__(self):
        info = f"Open remote file '{self.__filename}', mode '{self.__mode}' "
        info += f"at {hex(id(self.__fp))}"
        return info


with RemoteFile("server.log", "w")  as file:
    print(file)
    file.remote_write("Hello world!!!")
