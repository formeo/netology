import json

class FileJsonProcess:

    def __init__(self):
        pass

    def create_result_file(self,filename):
        result_file = open(filename, 'w',encoding='utf8')
        return result_file

    def write_into_file(self,file_descriptor,data):
        json.dump(data, file_descriptor, ensure_ascii=False)

    def close_file(self,file_descriptor):
         file_descriptor.close()

    def read_file(self,filename):
        with open(filename) as data_file:
            data = json.load(data_file)
        return data