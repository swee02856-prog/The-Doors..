# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Fonts', 'Fonts'), ('Apartments.png', '.'), ('ApartmentVoice1.mp3', '.'), ('ApartmentVoice2.mp3', '.'), ('ApartmentVoice3.mp3', '.'), ('ApartmentVoice4.mp3', '.'), ('ApartmentVoice5.mp3', '.'), ('backrooms1.mp3', '.'), ('backrooms2.mp3', '.'), ('backrooms3.mp3', '.'), ('backrooms4.mp3', '.'), ('backroomsbackground.png', '.'), ('BackroomVoice1.mp3', '.'), ('BackroomVoice2.mp3', '.'), ('BackroomVoice3.mp3', '.'), ('BackroomVoice4.mp3', '.'), ('BackroomVoice5.mp3', '.'), ('BlueDoor.png', '.'), ('BlueDoorOpened.png', '.'), ('choosingroom.mp3', '.'), ('default omnience.mp3', '.'), ('field.png', '.'), ('FieldVoice1.mp3', '.'), ('FieldVoice2.mp3', '.'), ('FieldVoice3.mp3', '.'), ('FieldVoice4.mp3', '.'), ('FieldVoice5.mp3', '.'), ('Jumpscare.mp3', '.'), ('Jumpscare.png', '.'), ('Neighborhood.png', '.'), ('NeighborhoodVoice1.mp3', '.'), ('NeighborhoodVoice2.mp3', '.'), ('NeighborhoodVoice3.mp3', '.'), ('NeighborhoodVoice4.mp3', '.'), ('NeighborhoodVoice5.mp3', '.'), ('next.mp3', '.'), ('Piperoom.png', '.'), ('PiperoomsVoice1.mp3', '.'), ('PiperoomsVoice2.mp3', '.'), ('PiperoomsVoice3.mp3', '.'), ('PiperoomsVoice4.mp3', '.'), ('PiperoomsVoice5.mp3', '.'), ('PoolRooms.png', '.'), ('PoolroomVoice1.mp3', '.'), ('PoolroomVoice2.mp3', '.'), ('PoolroomVoice3.mp3', '.'), ('PoolroomVoice4.mp3', '.'), ('PoolroomVoice5.mp3', '.'), ('RedDoor.png', '.'), ('RedDoorOpened.png', '.'), ('Textbox.png', '.'), ('Windowfloors.png', '.'), ('WindowroomVoice1.mp3', '.'), ('WindowroomVoice2.mp3', '.'), ('WindowroomVoice3.mp3', '.'), ('WindowroomVoice4.mp3', '.'), ('WindowroomVoice5.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Gloobls',
    debug=False,
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
)
