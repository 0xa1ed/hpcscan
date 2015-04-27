class wfyd:
    def __init__(self):
        self.procstart = ['C:\Users\mp\AppData\Local\Temp\wfyd.dll',
                'C:\Windows\System32\msiexec.exe',
                'C:\Users\mp\AppData\Local\Temp\KB00147241.exe']
        self.procterm = ['C:\Users\mp\AppData\Local\Temp\wfyd.dll',
                'C:\Users\mp\AppData\Local\Temp\KB00147241.exe']
        self.regset = ['HKCU\Software\Microsoft\Internet Explorer\LowRegistry\ErrorReporting\LastShipAssertTime',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\\1545094860',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\\1545094860',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth',
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
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows Defender',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Run\internat.exe']
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
        self.accuracy = 0.0
        self.origorder = [#'"C:\Program Files\Internet Explorer\iexplore.exe","SetValueKey","HKCU\Software\Microsoft\Internet Explorer\LowRegistry\ErrorReporting\LastShipAssertTime"',
                '"C:\Program Files\Internet Explorer\iexplore.exe","Write","C:\Users\mp\AppData\Local\Temp\wfyd.dll"',
                '"C:\Program Files\Internet Explorer\iexplore.exe","created","2980","C:\Users\mp\AppData\Local\Temp\wfyd.dll"',
                '"C:\Users\mp\AppData\Local\Temp\wfyd.dll","created","2992","C:\Users\mp\AppData\Local\Temp\wfyd.dll"',
                '"C:\Users\mp\AppData\Local\Temp\wfyd.dll","created","3016","C:\Windows\System32\msiexec.exe"',
                '"C:\Program Files\Internet Explorer\iexplore.exe","terminated","2980","C:\Users\mp\AppData\Local\Temp\wfyd.dll"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Windows"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Windows\System32\config\SOFTWARE.LOG1"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Windows\System32\config\SOFTWARE"',
                '"C:\Windows\System32\msiexec.exe","DeleteValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Run\\1545094860"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Windows\System32\config\SOFTWARE"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run\\1545094860"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Windows\System32\config\SOFTWARE"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\TaskbarNoNotification"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\HideSCAHealth"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Windows\System32\services.exe","Write","C:\\"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ShowSuperHidden"',
                '"C:\Windows\System32\msiexec.exe","SetValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Hidden"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Windows\System32\msiexec.exe","Write","C:\Users\mp\AppData\Local\Temp\KB00147241.exe"',
                '"C:\Users\mp\AppData\Local\Temp\wfyd.dll","created","3016","C:\Windows\System32\msiexec.exe"',
                '"C:\Windows\System32\msiexec.exe","created","3212","C:\Users\mp\AppData\Local\Temp\KB00147241.exe"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","Write","C:\Users\mp\Desktop\currently supported"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\UAC_bypassed"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Run\NdjGkxqc"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\AntiVirusOverride"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\AntiVirusDisableNotify"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\FirewallDisableNotify"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\FirewallOverride"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\UpdatesDisableNotify"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Security Center\UacDisableNotify"',
                '"C:\Windows\System32\\taskhost.exe","DeleteValueKey","HKCU\Software\Microsoft\Windows\CurrentVersion\Run\internat.exe"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\wscsvc\Start"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\EnableFirewall"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\DoNotAllowExceptions"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\SharedAccess\Parameters\FirewallPolicy\StandardProfile\DisableNotifications"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\wscsvc\Start"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","Delete","C:\Users\mp\Desktop\currently supported"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","Write","C:\Users\mp\AppData\Local\\fwrtauhl\\ndjgkxqc.exe"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","Write","C:\Users\mp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\ndjgkxqc.exe"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\WinDefend\Start"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\wuauserv\Start"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SYSTEM\ControlSet001\services\MpsSvc\Start"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","DeleteValueKey","HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows Defender"',
                '"C:\Users\mp\AppData\Local\Temp\KB00147241.exe","SetValueKey","HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config\SYSTEM.LOG1"',
                '"C:\Windows\System32\services.exe","Write","C:\Windows\System32\config"',
                '"C:\Users\mp\AppData\Local\Temp\wfyd.dll","terminated","2992","C:\Users\mp\AppData\Local\Temp\wfyd.dll"',
                '"System","Write","C:\Users\mp\AppData\Local\\fwrtauhl\\ndjgkxqc.exe"',
                '"System","Write","C:\Users\mp\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\ndjgkxqc.exe"',
                '"C:\Windows\System32\msiexec.exe","created","3212","C:\Users\mp\AppData\Local\Temp\KB00147241.exe"',
                '"C:\Windows\System32\msiexec.exe","terminated","3212","C:\Users\mp\AppData\Local\Temp\KB00147241.exe"']
        self.outbuff = []

    def getacc(self):
        accscore = 0.0
        if not self.outbuff or not self.origorder:
            return 0 
        else:
           # print self.outbuff[0]
            for i in range(0, len(self.outbuff)):
                if i < len(self.origorder):
                    if self.origorder[i] != self.outbuff[i]:
                        self.outbuff.insert(i, "0")
            for i in range(0, len(self.outbuff)):
                if i < len(self.origorder):
                    #print "comparing " + self.outbuff[i] + " and " + self.origorder[i]
                    if self.outbuff[i] == self.origorder[i]:
                    #    print "match"
                        accscore += 1
                    else:
                        pass
                else:
                    break
        if accscore == 0:
            return 0
        else:
            self.accuracy = accscore / len(self.origorder) * 100
            #print self.accuracy
        return self.accuracy
