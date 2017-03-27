# -*- mode: python -*-

block_cipher = None


a = Analysis(['my.py'],
             pathex=['E:\\ptest'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='my',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='Monkey_gorilla_16px_547305_easyicon.net.ico')
