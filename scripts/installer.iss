; KiraManager 安装包 —— Inno Setup 脚本
; 用法: ISCC.exe scripts\installer.iss

#define MyAppName "KiraManager"
#define MyAppVersion "0.6.0_dev"
#define MyAppPublisher "KiraAI"
#define MyAppURL "https://github.com/xxynet/KiraAI"
#define MyAppExeName "KiraManager.exe"

[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=..\dist
OutputBaseFilename=KiraManager_Setup_{#MyAppVersion}
SetupIconFile=..\kira_manager\app.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}:"; Flags: checkedonce

[Files]
Source: "..\dist\KiraManager\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\卸载 {#MyAppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "启动 {#MyAppName}"; Flags: postinstall nowait skipifsilent shellexec

[UninstallRun]
; 清理应用数据目录（配置、日志）
Filename: "{cmd}"; Parameters: "/c rmdir /s /q ""{userappdata}\KiraManager"""; Flags: runhidden

[Code]
function InitializeSetup: Boolean;
begin
  Result := True;
end;
