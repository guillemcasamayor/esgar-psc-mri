import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

TOKEN_FILE = r'C:\Users\gcasamayor\Downloads\05_Proyectos\gdrive-mcp-server\token.json'
creds = Credentials.from_authorized_user_file(TOKEN_FILE, ['https://www.googleapis.com/auth/drive'])
service = build('drive', 'v3', credentials=creds)

folder_id = '12MfxMAUUju7a7KH2HP1jS7rTnh_Ogj-I' # esgar_psc_mri in Google Drive
local_dir = r'C:\Users\gcasamayor\Downloads\05_Proyectos\esgar-psc-mri'

for filename in ['index.html', 'README.md']:
    file_path = os.path.join(local_dir, filename)
    if not os.path.exists(file_path):
        continue
    
    # Check if already exists in Drive folder to update or create
    q = f"'{folder_id}' in parents and name = '{filename}' and trashed = false"
    existing = service.files().list(q=q, fields='files(id, name)').execute().get('files', [])
    
    mimetype = 'text/html' if filename.endswith('.html') else 'text/markdown'
    media = MediaFileUpload(file_path, mimetype=mimetype, resumable=True)
    
    if existing:
        fid = existing[0]['id']
        updated = service.files().update(fileId=fid, media_body=media).execute()
        print(f"Actualizado en Drive: {filename} (ID: {fid})")
    else:
        created = service.files().create(
            body={'name': filename, 'parents': [folder_id]},
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        print(f"Subido a Drive: {filename} (ID: {created['id']})")

print("Sincronización completa con Google Drive.")
