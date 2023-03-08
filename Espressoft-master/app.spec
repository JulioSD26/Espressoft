# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['H:/Unison/Sexto semestre/PSI/Espressoft-master/app.py'],
    pathex=[],
    binaries=[],
    datas=[('H:/Unison/Sexto semestre/PSI/Espressoft-master/resources', 'resources/'), ('H:/Unison/Sexto semestre/PSI/Espressoft-master/resources/img', 'resources/img/'), ('H:/Unison/Sexto semestre/PSI/Espressoft-master/resources/fonts', 'resources/fonts/'), ('H:/dng20/api-ms-win-core-path-l1-1-0/api-ms-win-core-path-l1-1-0.dll', '.')],
    hiddenimports=['PyQt5', 'numpy', 'pyqtgraph', 'pywin32-ctypes', 'mkl-fft', 'mkl-service', 'mkl-random'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['H:\\dng20\\icono_cafe.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
