import requests
import os

# List of URLs to download
urls = [
    "https://dcc.ligo-wa.caltech.edu/public/0146/P1700349/001/H-H1_LOSC_CLN_16_V1-1187007040-2048.hdf5"
]

# Folder where you want to save the files
data_folder = os.path.join(os.getcwd(), "data")

# Ensure the 'data' folder exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Function to download files
def download_file(url):
    try:
        # Get the file name from the URL
        file_name = url.split('/')[-1]
        file_path = os.path.join(data_folder, file_name)
        
        # Send GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to a file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"File downloaded successfully: {file_name}")
        else:
            print(f"Failed to download {file_name}. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

# Loop through URLs and download each file
for url in urls:
    download_file(url)
