import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for name in files:
                print('Tranfering all files in this folder: ' + os.path.abspath(os.path.join(root, name)))
                print('To this folder in dropbox: ' + file_to)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
   
def main():
    access_token = 'QJnlTjHZFkcAAAAAAAAAAQLPFcinfUhBfMjg9viNsc94L4fwDsCapaUfkSf8J4NL'
    transferData = TransferData(access_token)

    file_from = input('Input file path of folder you want to transer: ')
    file_to = input('Input file path of the location in dropbox you want to transer to: ')

    transferData.upload_file(file_from, file_to)

main()