
import dropbox
import os

class transferData:
    def __init__(self, access_token):
        self.access_token=access_token
    
    for root, dirs, files in os.walk(fileFrom):
        relative_path = os.path.relpath(local_path, fileFrom)
        dropbox_path = os.path.join(fileTo, relativePath)
    def upload(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(fileFrom,'rb')
        dbx.files_upload(f.read(),fileTo)

def main():
    access_token='sl.A5nR1ljmFneHzeeiYh_GG1eCXO1FhbXBNkz-V44omqdk6Xx1ofOgZwGScDRyTDWwklO2N19O2s96VW8br5pG_mkOlGIfHRMXFX_aEc7GnKPmR_H-pNXgPSfYXOYb5tO0N9S7jMk'
    transferdata=transferData(access_token)
    fileFrom=input("Enter the File Path to Upload: ")
    fileTo=input("The Entire Path to Upload to Dropbox: ")
    transferdata.upload(fileFrom,fileTo)
    print("File Transferred Successfully")

main()