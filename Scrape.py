import pandas as pd
from pytube import YouTube

# Function to get video information
def get_video_info(url):
    try:
        yt = YouTube(url)
        length = yt.length  # Video length in seconds
        upload_date = yt.publish_date  # Upload date
        return length, upload_date
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None, None

# Function to update spreadsheet with video information
def update_spreadsheet(input_file, output_file):
    # Read the spreadsheet
    df = pd.read_excel(input_file)  # Change the file type if needed (e.g., pd.read_csv for CSV files)

    # Add columns for video length and upload date
    df['Video Length'] = None
    df['Upload Date'] = None

    # Update each row with video information
    for index, row in df.iterrows():
        video_url = row['Video Link']
        length, upload_date = get_video_info(video_url)

        # Update the corresponding row with video information
        df.at[index, 'Video Length'] = length
        df.at[index, 'Upload Date'] = upload_date

    # Save the updated dataframe to a new spreadsheet
    df.to_excel(output_file, index=False)  # Change the file type if needed (e.g., df.to_csv for CSV files)

input_file_path = 'Links.xlsx'  # Replace with the path to your input spreadsheet
output_file_path = 'Data.xlsx'  # Replace with the desired output spreadsheet path

update_spreadsheet(input_file_path, output_file_path)