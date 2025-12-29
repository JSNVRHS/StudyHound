# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\studyHoundMenu.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\images\\StudyHoundBlackNoBG.png', 'images'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\images\\StudyHoundFullLogoBlack.png', 'images'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\images\\StudyHoundFullLogoOriginal.png', 'images'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\images\\StudyHoundLogo.png', 'images'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\images\\StudyHoundNoBG.png', 'images'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\records\\history.txt', 'records'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\settings.txt', '.'), ('C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\studyHound.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='studyHoundMenu',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Ataye\\OneDrive\\Desktop\\Python\\StudyHoundByDZJU2B\\StudyHound.ico'],
)
