import base64
import wget
def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    return resultUrl

onedrive_url = "https://1drv.ms/b/s!Aocxj1Hi_hVIldlmDgRjNJq97gLZog?e=QbTV4O"
# Generate Direct Download URL from above Script
direct_download_url = create_onedrive_directdownload(onedrive_url)

print('Downloading dataset')
r = wget.download(direct_download_url,out='./rt/')
print('\n')
print(r)