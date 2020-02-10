# -*- mode: python -*-

block_cipher = None


a = Analysis(['VICREO_Listener_OSX.py'],
             pathex=['/Users/rob/Documents/VICREO-Listener'],
             binaries=[],
             datas=[('icon.icns','/Users/rob/Documents/VICREO-Listener/icon.icns')],
             hiddenimports=['rumps','pynput.keyboard','psutil'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VICREO Listener',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
app = BUNDLE(exe,
             name='VICREO Listener.app',
             icon='/Users/rob/Documents/VICREO-Listener/icon.icns',
             bundle_identifier=None,
             info_plist={
                'LSUIElement': 'True',
                'NSHighResolutionCapable': 'True',
                'CFBundleShortVersionString': '1.4.0',
                'NSHumanReadableCopyright': 'Copyright © 2019, Jeffrey Davidsz. All rights reserved.'
            },
        )
