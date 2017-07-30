import os
import socket
import boto3

BUCKET = "myproject-backups"
S3_DIRECTORY = socket.gethostname()
DB_BACKUP_FILE = "myproject_postgres_1.sql"
DB_BACKUP_PATH = "/tmp/{filename}".format(filename=DB_BACKUP_FILE)
DB_S3_DIRECTORY = "{directory}/postgresql".format(directory=S3_DIRECTORY)

s3 = boto3.resource('s3')

os.system("docker exec -u postgres myproject_postgres_1 pg_dumpall > {path}".format(path=DB_BACKUP_PATH))

backup = open(DB_BACKUP_PATH, "rb")
s3.Object(BUCKET, "{directory}/{filename}".format(directory=DB_S3_DIRECTORY, filename=DB_BACKUP_FILE)).put(Body=backup)