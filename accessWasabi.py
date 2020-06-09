
# make sure to pip install git+https://github.com/KalobMTaulien/boto3_wasabi
import boto3_wasabi

WASABI_ACCESS_KEY= 'V4C447EX2LG7J5UM6LAJ'
WASABI_SECRET_KEY= 'wY5NzWdZB4CHhZu83HJVHrHJYMyVCL1UK1FY1sbI'
WASABI_BUCKET = 'data-lake-sbillinge'

#take this example tiff filename out of the ifname=name section and insert another filename in the working directory
EXAMPLE_TIFF = 'zthatcher_image.tif'


class WasabiInterface(object):

    def __init__(self):
        self._accessKey = WASABI_ACCESS_KEY
        self._privateKey = WASABI_SECRET_KEY
        self._bucketName = WASABI_BUCKET

    def file_write(self, filename=EXAMPLE_TIFF):
        """
        Takes in a filename from the working directory as an argument and uploads it to wasabi
        :param filename:
        :return:
        """
        # Start the boto3 client that points to Wasabi's S3 endpoints.
        s3 = boto3_wasabi.client('s3', aws_access_key_id=self._accessKey, aws_secret_access_key=self._privateKey)
        # Open the file as readable
        with open(filename, 'rb') as body:
            # Upload your file
            upload_data = s3.put_object(Bucket=self._bucketName, Key=filename, Body=body, ContentType='text/plain')

        # Print the uploaded data
        return upload_data

    def file_read(self, filetoretrieve=EXAMPLE_TIFF, newfilename='Downloadedfile.tif'):
        """
        Retrieves a file from wasabi and puts it in the current working directory
        :param filetoretrieve:
        :param newfilename:
        :return:
        """
        # Start the boto3 client that points to Wasabi's S3 endpoints.
        s3 = boto3_wasabi.client('s3', aws_access_key_id=self._accessKey, aws_secret_access_key=self._privateKey)
        # Open the file as write-able
        with open(newfilename, 'wb') as body:
            output = s3.download_fileobj(self._bucketName, filetoretrieve, body)

        # Print to signify that script ran
        print('...Downloaded')
        return output

    def file_delete(self, filetoretdelete=EXAMPLE_TIFF):
        s3 = boto3_wasabi.client('s3', aws_access_key_id=self._accessKey, aws_secret_access_key=self._privateKey)
        output = s3.delete_object(Bucket=self._bucketName, Key=filetoretdelete)
        print(output)

if __name__ == "__main__":
    wasabi = WasabiInterface()
    #wasabi.file_delete(EXAMPLE_TIFF)
    #wasabi.file_write(EXAMPLE_TIFF)
    #wasabi.file_read(EXAMPLE_TIFF, 'Downloadedfile.tif')
