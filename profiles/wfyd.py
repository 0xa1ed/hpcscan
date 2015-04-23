class wfyd:
    def __init__(self):
        self.procstart = ['C:\Users\mp\AppData\Local\Temp\wfyd.dll',
                'C:\Windows\System32\msiexec.exe',
                'C:\Users\mp\AppData\Local\Temp\KB00147241.exe']
        self.procterm = ['C:\Users\mp\AppData\Local\Temp\wfyd.dll',
                'C:\Users\mp\AppData\Local\Temp\KB00147241.exe']
        self.regset = ['HKCU\Software\Microsoft\Internet Explorer\LowRegistry\ErrorReporting\LastShipAssertTime',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\\1545094860',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth',
                'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UAC_bypassed',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowSuperHidden',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Hidden',
                'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UAC_bypassed',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Run\NdjGkxqc',
                'HKLM\SOFTWARE\Microsoft\Security Center\AntiVirusOverride',
                'HKLM\SOFTWARE\Microsoft\Security Center\AntiVirusDisableNotify',
                'HKLM\SOFTWARE\Microsoft\Security Center\FirewallDisableNotify',
                'HKLM\SOFTWARE\Microsoft\Security Center\FirewallOverride',
                'HKLM\SOFTWARE\Microsoft\Security Center\UpdatesDisableNotify',
                'HKLM\SOFTWARE\Microsoft\Security Center\UacDisableNotify',
                'HKLM\SYSTEM\ControlSet001\services\wscsvc\Start',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Run\internat.exe',
                'HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\EnableFirewall',
                'HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\DoNotAllowExceptions',
                'HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\DisableNotifications',
                'HKLM\SYSTEM\ControlSet001\services\WinDefend\Start',
                'HKLM\SYSTEM\ControlSet001\services\wuauserv\Start',
                'HKLM\SYSTEM\ControlSet001\services\MpsSvc\Start',
                'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit']
        self.regdel = ['HKCU\Software\Microsoft\Windows\CurrentVersion\Run\\1545094860',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows Defender']
        self.filewrite = ['C:\Users\mp\AppData\Local\Temp\wfyd.dll',
                'C:\Windows',
                'C:\Windows\System32\config\SOFTWARE.LOG1',
                'C:\Windows\System32\config\SOFTWARE',
                'C:\Windows\System32\config',
                'C:\\',
                'C:\Windows\System32\config\SYSTEM.LOG1',
                'C:\Users\mp\AppData\Local\Temp\KB00147241.exe',
                'C:\Users\mp\Desktop\currently supported',
                'C:\Users\mp\AppData\Local\\fwrtauhl\\ndjgkxqc.exe',
                'C:\Users\mp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\ndjgkxqc.exe']
        self.filedel = ['C:\Users\mp\Desktop\currently supported']
        self.score = 0
        self.accuracy = 0
        self.origorder = []
        self.outbuff = []

    def getacc():
        return accuracy
