#pylint:disable=no-member

import os
import shutil

from google.cloud import storage

# Path of the current directory
path_of_the_directory = 'TODO'

# Set your Google Cloud project ID and the path to your service account key JSON file
project_id = 'TODO'
keyfile_path = 'TODO/keyfile.json'  # Update with the actual path

# Initialize a client using the credentials in the JSON key file
client = storage.Client.from_service_account_json(keyfile_path, project=project_id)

# Specify the name of the Google Cloud Storage bucket and the image file to upload
bucket_name = 'TODO'

if not os.path.exists(path_of_the_directory):
    os.makedirs(path_of_the_directory)

with os.scandir(path_of_the_directory) as entries:
    file_names = [entry.name for entry in entries if entry.is_file()]

entries.close()

sorted_file_names = sorted(file_names, key=lambda s: s.lower())

pic_to_upload = ''

print("Scanning files in '% s':" % path_of_the_directory)
for file_name in sorted_file_names:
    print(file_name)
    if pic_to_upload != file_name[0:14]:
        pic_to_upload = file_name[0:14]
        # Upload the image to the bucket
        try:
            bucket = client.get_bucket(bucket_name)
            destination_blob_name = pic_to_upload + ".jpg"
            print(f"Attempting to upload to image: {destination_blob_name}")
            blob = bucket.blob(destination_blob_name)
    
            # Upload the image
            image_file_path = path_of_the_directory + file_name
            print(f"Attempting to upload from image: {image_file_path}")
            blob.upload_from_filename(image_file_path)
            print(f"Image uploaded to {bucket_name}/{destination_blob_name}")
        except Exception as e:
            print(f"Error uploading image: {e}")

    new_pic_folder = file_name[0:8] + '/'
        
    if not os.path.exists(path_of_the_directory + new_pic_folder):
        os.makedirs(path_of_the_directory + new_pic_folder)   
    shutil.move(path_of_the_directory + file_name, path_of_the_directory + new_pic_folder + file_name)
