# Kira Environment Manager

KiraAI 桌面管理工具 — 一键下载、配置、运行和管理多个 KiraAI 实例。

基于 PyQt5 + qfluentwidgets 构建。

## 功能

- **环境配置** — Python 检测、pip 镜像源测速/切换、venv 创建、依赖安装
- **项目管理** — 从 GitHub 克隆/拉取 KiraAI、版本检测
- **启动管理** — 多实例管理、端口检测、WebUI 浏览器启动
- **浏览器** — 快速打开 KiraAI WebUI
- **日志查看** — 自动刷新日志，方便排查

## 快速开始

```bash
# 安装依赖
pip install PyQt5 qfluentwidgets

# 运行
python kira_env_manager/main.py
```

## 构建安装包

```bash
# 1. PyInstaller 打包
pyinstaller KiraEnvManager.spec --clean --noconfirm

# 2. Inno Setup 制作安装包
ISCC.exe scripts\installer.iss
```

## License

AGPL-3.0
