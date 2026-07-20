import os
import shutil
import glob

print("Cleaning temporary files and caches to free disk space...")

# 1. Clean dist and .astro
for path in ['dist', '.astro', 'node_modules/.cache']:
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"Removed: {path}")
        except Exception as e:
            print(f"Error removing {path}: {e}")

# 2. Clean zip backups in backups/
for zip_file in glob.glob("backups/*.zip"):
    try:
        os.remove(zip_file)
        print(f"Removed zip backup: {zip_file}")
    except Exception as e:
        print(f"Error removing {zip_file}: {e}")

# 3. Clean temporary files in system Temp directory if possible
temp_dir = os.environ.get("TEMP", "")
if temp_dir and os.path.exists(temp_dir):
    print(f"Checking temp dir: {temp_dir}")
    # Remove files starting with tmp or astro or vite in Temp
    for f in glob.glob(os.path.join(temp_dir, "*astro*")) + glob.glob(os.path.join(temp_dir, "*vite*")):
        try:
            if os.path.isfile(f):
                os.remove(f)
            elif os.path.isdir(f):
                shutil.rmtree(f, ignore_errors=True)
            print(f"Cleaned temp file: {os.path.basename(f)}")
        except Exception as e:
            pass

print("Cleanup finished!")
