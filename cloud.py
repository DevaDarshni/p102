import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGTVzCqKJvK4c-H20VChLjMjovkx7bdN74FRDfl6Tn0VRbqeSivC4rQjZbHNgYu06veB1l9WPXpmoJAqDT3J1KOSCqbAp37bm8i1vtdEgGd0xOUkDOPcdCDZHgfgsdxnb7Xylk7nbGwt'
    transferData = TransferData(access_token)
    
    file_from=input("enter the file path: ")
    file_to=input("enter the full file path")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file upload")

if __name__ == '__main__':
    main()