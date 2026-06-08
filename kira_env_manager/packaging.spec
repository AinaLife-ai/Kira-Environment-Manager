# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller 打包配置 — Kira Environment Manager

用法（从 kira_env_manager 目录执行）:
    cd kira_env_manager  &&  pyinstaller packaging.spec

输出:
    dist/KiraEnvManager.exe
"""

import os
import sys
from pathlib import Path

# ── 路径基础 ──────────────────────────────────────────────────────────────
# spec 上下文中 __file__ 不可用，但 os.getcwd() 可用（前提是从 kira_env_manager 目录运行）
CWD = Path(os.getcwd()).resolve()
APP_ICO = CWD / "app.ico"

# ── 收集 qfluentwidgets 数据资源 ─────────────────────────────────────────────
import qfluentwidgets

QFW_ROOT = Path(qfluentwidgets.__file__).resolve().parent
QFW_DATA = [
    # qfluentwidgets/_rc 包含编译好的 QSS、图标、翻译等资源
    (str(QFW_ROOT / "_rc"), "qfluentwidgets/_rc"),
]

# ── 主配置 ──────────────────────────────────────────────────────────────────
a = Analysis(
    ["main.py"],
    pathex=[
        # qfluentwidgets 是 editable 安装，不在 site-packages 中，
        # 需要显式添加父仓库路径供 PyInstaller 搜索
        str(CWD.parent.parent),       # PyQt-Fluent-Widgets-master
    ],
    binaries=[],
    datas=QFW_DATA,
    hiddenimports=[
        # qfluentwidgets 隐式子模块
        "qfluentwidgets",
        "qfluentwidgets.common",
        "qfluentwidgets.common.icon",
        "qfluentwidgets.common.style_sheet",
        "qfluentwidgets.common.config",
        "qfluentwidgets.common.router",
        "qfluentwidgets.common.animation",
        "qfluentwidgets.common.translator",
        "qfluentwidgets.common.color",
        "qfluentwidgets.common.font",
        "qfluentwidgets.common.theme_listener",
        "qfluentwidgets.components",
        "qfluentwidgets.components.widgets",
        "qfluentwidgets.components.navigation",
        "qfluentwidgets.components.dialog_box",
        "qfluentwidgets.components.settings",
        "qfluentwidgets.components.layout",
        "qfluentwidgets.components.date_time",
        "qfluentwidgets.window",
        "qfluentwidgets._rc",
        # PyQt5 额外模块（在冻结模式下可能需显式指定）
        "PyQt5.QtCore",
        "PyQt5.QtGui",
        "PyQt5.QtWidgets",
        "PyQt5.QtNetwork",
        
        # darkdetect（qfluentwidgets 依赖的 OS 主题检测库）
        "darkdetect",
        # 内置模块（被动态 import 引用）
        "venv",
        "threading",
        "logging.handlers",
        "urllib.request",
        "html",
        "shutil",
        "signal",
        "webbrowser",
        "socket",
        "re",
        "json",
        "copy",
        "time",
        "datetime",
    ],
    hookspath=[],
    hooksconfig={},
    excludes=[
        # 排除不必要的模块以减小体积
        # 注意: qfluentwidgets 可能依赖 QtXml/QtSvg/QtPrintSupport 等，
        # 不要轻易添加 Qt 模块到 excludes 列表
        "PyQt5.QtBluetooth",
        "PyQt5.QtHelp",
        "PyQt5.QtLocation",
        "PyQt5.QtMultimediaWidgets",
        "PyQt5.QtNfc",
        "PyQt5.QtPositioning",
        "PyQt5.QtQml",
        "PyQt5.QtQuick",
        "PyQt5.QtQuick3D",
        "PyQt5.QtRemoteObjects",
        "PyQt5.QtSensors",
        "PyQt5.QtSerialPort",
        "PyQt5.QtWebChannel",
        "PyQt5.QtWebEngine",
        "PyQt5.QtWebEngineWidgets",
        "PyQt5.QtWebSockets",
        "tkinter",
        "turtle",
        "test",
        "distutils",
        "setuptools",
        "scipy",
        "matplotlib",
        "notebook",
        "jupyter",
        "ipython",
        "pandas",
        "PIL",
        "cv2",
        "tornado",
    ],
    noarchive=False,
)

# ── 收集 PyQt5 必要的动态库 ──────────────────────────────────────────────────
# PyQt5.QtNetwork 是 qfluentwidgets 内部可能用到的网络模块
# PyQt5.QtMultimedia 是可选的，但保留以兼容
for mod_name in ("PyQt5.QtNetwork",  "PyQt5.QtGui"):
    try:
        __import__(mod_name)
    except ImportError:
        a.hiddenimports.append(mod_name)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="KiraEnvManager",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # Windows GUI 模式，不显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(APP_ICO) if APP_ICO.exists() else None,
)

# ── 如果需要单文件模式，取消下面注释并注释上面的 EXE ─────────────────────────
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name="KiraEnvManager",
# )
