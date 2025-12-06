# extensions.py

# Prompt the user for the file name
filename = input("File name: ").strip().lower()

# Define known media types
media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Find the extension (if any)
if '.' in filename:
    ext = '.' + filename.split('.')[-1]
    print(media_types.get(ext, "application/octet-stream"))
else:
    print("application/octet-stream")
