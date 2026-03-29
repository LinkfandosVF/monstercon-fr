import os
 
FRENCH_DIR = os.path.expanduser("~/Desktop/monsterprom_fr/french")
 
for filename in os.listdir(FRENCH_DIR):
    if filename.startswith("english_"):
        new_name = filename.replace("english_", "french_", 1)
        os.rename(
            os.path.join(FRENCH_DIR, filename),
            os.path.join(FRENCH_DIR, new_name)
        )
        print(f"  {filename} → {new_name}")
 
print("\nDone!")
print("sale flemmard...")