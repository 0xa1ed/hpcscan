class mailvir:
    def __init__(self):
        self.procstart = ['C:\Users\mp\AppData\Local\Temp\\fqcuk.dll',
                'C:\Users\mp\AppData\Roaming\Qohezy\zeve.exe',
                'C:\Program Files\Windows Mail\WinMail.exe',
                'C:\Users\mp\AppData\Local\Temp\BHDG.dll']
        self.procterm = ['C:\Users\mp\AppData\Local\Temp\\fqcuk.dll']
        self.regset = ['HKCU\Software\Microsoft\Internet Explorer\LowRegistry\ErrorReporting\LastShipAssertTime',
                'HKCU',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\IndexTable\FileIdIndex-{41003fa5-89a3-11e3-bfdc-806e6f6e6963}\_IndexName_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\_CurrentObjectId_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\_ObjectId_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\LruList\CurrentLru',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\LruList\\0000000000000B73\ObjectId',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\LruList\\0000000000000B73\ObjectLru',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\_ObjectLru_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\_FileId_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\_Usn_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\_UsnJournalId_',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\Indexes\FileIdIndex-{41003fa5-89a3-11e3-bfdc-806e6f6e6963}\900000000A149',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\IndexTable\FileIdIndex-{41003fa5-89a3-11e3-bfdc-806e6f6e6963}\900000000A149\\13D',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\AeFileID',
                '\REGISTRY\A\{511E200C-167F-11E4-9376-080027E9ED50}\DefaultObjectStore\ObjectTable\\13D\AeProgramID',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\3\\1406',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\1\\1609',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\4\\1A02',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\2\\1A10',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\4\\1A10',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\4\\1A03',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\3\\1A05',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\4\\1A05',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\4\\1A06',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Lockdown_Zones\\0\\1609'
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\WarnonBadCertRecving'
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\EnableSPDY3_0',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\UNCAsIntranet',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\AutoDetect',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\\0\\1609',
                'HKCU\Software\Microsoft\Nylaiw\Fauzwua',
                'HKCU\Software\Microsoft\Nylaiw\Upcaolap',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyEnable',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections\SavedLegacySettings',
                'HKCU\Software\Microsoft\IAM\Accounts\ConnectionSettingsMigrated',
                'HKCU\Software\Microsoft\Windows Mail\Trident\Main\Move System Caret',
                'HKCU\Software\Microsoft\Windows Mail\StoreMigratedV5',
                'HKCU\Software\Microsoft\Windows Mail\Settings Upgraded',
                'HKCU\Software\Microsoft\Windows Mail\Mail\Safe Attachments',
                'HKCU\Software\Microsoft\Windows Mail\Mail\Secure Safe Attachments',
                'HKCU\Software\Microsoft\Windows Mail\Running',
                'HKCU\Software\Microsoft\IAM\Default LDAP Account',
                'HKCU\Software\Microsoft\IAM\Server ID',
                'HKCU\Identities\{ACC29697-975F-4790-9CF9-A615892A2859}\Identity Ordinal',
                'HKCU\Identities\Identity Ordinal',
                'HKCU\Software\Microsoft\Windows Mail\LastBackup',
                'HKCU\Software\Microsoft\Windows Mail\V7StoreMigDone',
                'HKCU\Software\Microsoft\IAM\Default News Account',
                'HKCU\Software\Microsoft\WAB\NamedProps',
                'HKCU\Software\Microsoft\WAB\NamedPropCount',
                'HKCU\Software\Microsoft\Windows Mail\Mail\Welcome Message',
                'HKCU\Software\Microsoft\Windows Mail\Junk Mail\Safe Senders List\Version',
                'HKCU\Software\Microsoft\Windows Mail\Junk Mail\Block Senders List\Version',
                'HKCU\Software\Microsoft\IdentityCRL\Dynamic Salt\Value',
                'HKCU\Software\Microsoft\IdentityCRL\Dynamic Salt\Size',
                'HKCR\Local Settings\MuiCache\B\\52C64B7E\LanguageList',
                'HKCU\Software\Microsoft\Windows Mail\SpoolerDlgPos',
                'HKCU\Software\Microsoft\Windows Mail\SpoolerTack',
                'HKCU\Software\Microsoft\Windows Mail\Mail\Default_CodePage',
                'HKCU\Software\Microsoft\Windows Mail\Compact Check Count',
                'HKCU\Software\Microsoft\Windows Mail\LastRun',
                ]

        self.regdel = ['HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProxyBypass',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProxyBypass',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\IntranetName',
                'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\IntranetName',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Run\zeve.exe',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyServer',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyOverride',
                'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\AutoConfigURL',
                'HKCU\Identities\OutgoingID',
                'HKCU\Identities\Changing',
                'HKCU\Identities\IncomingID',
                'HKCU\Software\Microsoft\WAB\NamedProps',
                'HKCU\Software\Microsoft\WAB\NamedPropCount',
                ]
        self.filewrite = ['C:\Users\mp\AppData\Local\Temp\\fqcuk.dll',
                'C:\Users\mp\AppData\Roaming\Qohezy\zeve.exe',
                'C:\Windows\AppCompat\Programs\RecentFileCache.bcf',
                'C:\Users\mp\AppData\Local\Temp\\tmp4632b6f2.bat',
                'C:\Program Files\Capture\logs\deleted_files\C\Users\mp\AppData\Local\Temp\\tmp4632b6f2.bat',
                'C:\Users\mp\AppData\Local\Temp\BHDG.dll',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\edb.log',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\\tmp.edb',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\WindowsMail.MSMessageStore',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\\temp\WindowsMail.MSMessageStore',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\edbtmp.log',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\WindowsMail.pat',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\\temp\edb00002.log',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\\temp\WindowsMail.pat',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Inbox\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Outbox\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Sent Items\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Deleted Items\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Drafts\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Junk E-mail\winmail.fol',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Local Folders\Inbox\\4F8B02F0-00000001.eml',
                'C:\Users\mp\AppData\Roaming\Microsoft\Protect\S-1-5-21-78034117-1329648361-637219273-1001\\3aed1323-c5d3-4c4a-979c-78f92d2e3e2b',
                'C:\Users\mp\AppData\Roaming\Microsoft\Protect\S-1-5-21-78034117-1329648361-637219273-1001\Preferred',
                'C:\Users\mp\AppData\LocalLow\Microsoft\CryptnetUrlCache\MetaData\E6024EAC88E6B6165D49FE3C95ADD735',
                'C:\Users\mp\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content\E6024EAC88E6B6165D49FE3C95ADD735',
                'C:\Users\mp\AppData\Local\Temp\CabF8E.tmp',
                'C:\Users\mp\AppData\Local\Temp\TarF8F.tmp',
                'C:\Users\mp\AppData\Local\Temp\ppcrlui_3164_2',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\edb.chk'
                ]
        self.filedel = ['C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\old\edb00001.log',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\old\WindowsMail.MSMessageStore',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\old\WindowsMail.pat',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\Backup\old',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\edb00001.log',
                'C:\Users\mp\AppData\Local\Temp\CabF8E.tmp',
                'C:\Users\mp\AppData\Local\Temp\TarF8F.tmp',
                'C:\Users\mp\AppData\Local\Temp\ppcrlui_3164_2.ui',
                'C:\Users\mp\AppData\Local\Temp\ppcrlui_3164_2',
                'C:\Users\mp\AppData\Local\Microsoft\Windows Mail\edbtmp.log']
        self.score = 0
        self.accuracy = 0
        self.origorder = []
        self.outbuff = []

    def getacc():
        accscore = 0
        if len(outbuff) == 0:
            accuracy = 100
            return accuracy
        else:
            for i in range(0, len(outbuff)):
                if i > len(outbuff) or i > len(origorder):
                    break
                else:
                    if outbuff[i] == origorder[i]:
                        accscore += 1
                    else:
                        pass
        accuracy = accscore / len(origorder) * 100
        return accuracy
