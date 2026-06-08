# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('kira_manager/app.ico', 'kira_manager'), ('kira_manager/fonts/苹方字体.ttf', 'kira_manager/fonts')]
binaries = []
hiddenimports = ['kira_manager', 'kira_manager.view', 'kira_manager.view.main_window', 'kira_manager.view.home_page', 'kira_manager.view.env_page', 'kira_manager.view.project_page', 'kira_manager.view.launch_page', 'kira_manager.view.browser_page', 'kira_manager.view.log_page', 'kira_manager.view.config_page', 'kira_manager.utils', 'kira_manager.utils.instance_manager', 'kira_manager.utils.process_manager', 'kira_manager.utils.python_env', 'kira_manager.utils.project', 'kira_manager.utils.network', 'kira_manager.utils.pip_mirrors', 'kira_manager.utils.logger', 'kira_manager.utils.helpers', 'kira_manager.common', 'kira_manager.common.config', 'kira_manager.common.constants', 'darkdetect', 'PyQt5.QtSvg', 'PyQt5.QtNetwork']
tmp_ret = collect_all('qfluentwidgets')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['kira_manager\\main.py'],
    pathex=['C:\\Users\\Administrator\\Desktop\\PyQt-Fluent-Widgets-master'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5.QtBluetooth', 'PyQt5.QtDBus', 'PyQt5.QtDesigner', 'PyQt5.QtHelp', 'PyQt5.QtLocation', 'PyQt5.QtMultimedia', 'PyQt5.QtMultimediaWidgets', 'PyQt5.QtNfc', 'PyQt5.QtOpenGL', 'PyQt5.QtPositioning', 'PyQt5.QtPrintSupport', 'PyQt5.QtQml', 'PyQt5.QtQuick', 'PyQt5.QtQuickWidgets', 'PyQt5.QtRemoteObjects', 'PyQt5.QtSensors', 'PyQt5.QtSerialPort', 'PyQt5.QtSql', 'PyQt5.QtTest', 'PyQt5.QtWebChannel', 'PyQt5.QtWebSockets', 'PyQt5.QtXmlPatterns', 'PyQt5.uic', 'matplotlib', 'notebook', 'jupyter', 'Crypto', 'cryptography', 'boto3', 'botocore', 'zmq', 'tornado', 'prompt_toolkit', 'setuptools', 'wheel', 'pip', 'pkg_resources'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KiraManager',
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
    icon=['kira_manager\\app.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='KiraManager',
)
