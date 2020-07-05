import ftplib

def main(filename, ipaddress, username, password, filepath):

    filename = str(filename)

    ftp = ftplib.FTP(str(ipaddress)) #ipaddress

    ftp.login(str(username), str(password)) #username, password

    ftp.cwd('files')

    myfile = open(str(filepath), 'rb') # filepath

    ftp.storbinary('STOR ' + filename, myfile)
