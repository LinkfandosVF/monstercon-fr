import UnityPy

BUNDLE_PATH = "/Applications/MonsterProm4 but baguette.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/texts_assets_all.bundle"

env = UnityPy.load(BUNDLE_PATH)

print(f"Assets trouvés : {len(env.objects)}\n")

for obj in env.objects:
    if obj.type.name == "TextAsset":
        data = obj.read()
        raw = data.m_Script
        if isinstance(raw, bytes):
            raw = raw.decode('utf-8', errors='replace')
        text_preview = str(raw)[:80].replace('\n', ' ') if raw else "(vide)"
        print(f"  [{obj.path_id}] {data.m_Name} → {text_preview}")
