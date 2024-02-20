# File Transfer Module

## Overview
The File Transfer module automates the process of uploading files to cloud storage services. It supports AWS S3 for images and media files, and Google Cloud Storage for document files. The module scans a specified directory (and its subdirectories) for files matching predefined extensions and uploads them to the respective cloud storage service based on the file type.

## Features
- Scans directories recursively for files.
- Configurable file extensions for AWS S3 and Google Cloud Storage.
- Uploads images and media files to AWS S3.
- Uploads document files to Google Cloud Storage.

## Prerequisites
- Python 3.x
- AWS account with S3 access
- Google Cloud account with Storage access
- `boto3` and `google-cloud-storage` Python libraries

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd path/to/project


Ensure AWS and Google Cloud credentials are correctly configured in your environment. 
For AWS, configure credentials using the AWS CLI (aws configure). 
For Google Cloud, set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your service account key file.


##Usage
To use the module, you can write a Python script that imports and calls the upload_files function from the file_transfer.uploader module. Here's an example:
'''
    from file_transfer.uploader import upload_files

    directory = '/path/to/your/directory'
    upload_files(directory)
'''