import UnityPy
env = UnityPy.load('/Applications/Monster Prom 4 Monster Con.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/texts_assets_all.bundle')
print(type(env.file))
print([a for a in dir(env.file) if not a.startswith('_')])
