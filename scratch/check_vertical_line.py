import os
import zipfile
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
zip_filename = f"backups/astro_site_backup_{timestamp}.zip"

os.makedirs("backups", exist_ok=True)

# Use ZIP_STORED for instantaneous uncompressed zip backup of source code and public assets
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_STORED) as zipf:
    for root, dirs, files in os.walk('.'):
        if any(ignored in root for ignored in ['node_modules', 'dist', '.astro', '.git', 'backups']):
            continue
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, file_path)

print(f"Created fast backup archive: {zip_filename}")
