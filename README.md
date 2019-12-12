# Personal_Software_List
因为每次装机都要一个一个找以前装过的软件，索性列一个清单，加快装机效率

哈希值校验语法：CertUtil -hashfile 路径 MD2/MD4/MD5/SHA1/SHA256/SHA384/SHA512

CPU核数设置:msconfig

卓越性能:<pre>powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61</pre>

一键设置所有uwp应用使用代理（用cmd）：
<pre>FOR /F "tokens=11 delims=\" %p IN ('REG QUERY "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings"') DO CheckNetIsolation.exe LoopbackExempt -a -p=%p</pre>

<pre>Windows Registry Editor Version 5.00

;如需还原去除上语句前减号即可

;取消我的电脑"视频"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}]

;取消我的电脑"文档"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}]

;取消我的电脑"桌面"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}]

;取消我的电脑"音乐"文件夹?

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}]

;取消我的电脑"下载"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}]

;取消我的电脑"图片"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}]

;取消我的电脑"3D对象"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}]</pre>

<pre>Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ReserveManager]
"ShippedWithReserves"=dword:00000000</pre>

<pre>Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]

"FeatureSettings"=dword:00000003

"FeatureSettingsOverrideMask"=dword:00000003</pre>

<pre>-i
--proxy socks5://127.0.0.1:2080/
-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
-o V:/annie/"%(uploader)s (%(uploader_id)s)/%(upload_date)s - %(title)s - (%(duration)ss) [%(resolution)s] [%(id)s].%(ext)s"
--add-metadata
--write-description
--write-thumbnail
</pre>

<pre>
Windows Registry Editor Version 5.00

;导入Flash优化设置 支持Chromium/Chrome .

;AllowOutdatedPlugins	是否允许加载过期的Flash插件，1表示允许，0表示禁止，建议开启，避免flash狂刷版本号，频繁更新，根据自身情况酌情修改
;RunAllFlashInAllowMode	如果启用此设置（即设置为1），那么在内容设置中设为允许运行 Flash（无论是由用户还是由企业政策设置）的网站中内嵌的所有 Flash 内容（包括来自其他来源的内容或不重要的内容）都会运行。
;DefaultPluginsSetting	默认Flash设置，1 = 强制所有网站自动运行 Flash 插件，且用户无法再设置中关闭，2 = 禁止 Flash 插件运行，3 = 点击运行，类似先提示再运行
;HardwareAccelerationModeEnabled	启用硬件加速，即使用GPU渲染网页,打开对3D 图形 API 的支持，1为开，0为关
;PluginsAllowedForUrls	强制允许Flash运行的白名单网站，即该项下面的值。键值名表示第几项规则序号，键值内容为白名单网站，我已经帮你匹配了所有域名了。
;特别说明：PluginsAllowedForUrls和DefaultPluginsSetting是结合使用的，两者不能分开，单独设置DefaultPluginsSetting是无效的，强制开启必须同时指定强制运行的白名单网址


;Chromium需要导入到User这个根键下面，否则不生效
[HKEY_CURRENT_USER\SOFTWARE\Policies\Chromium]
"AllowOutdatedPlugins"=dword:00000001
"RunAllFlashInAllowMode"=dword:00000001
"DefaultPluginsSetting"=dword:00000001
"HardwareAccelerationModeEnabled"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Policies\Chromium\PluginsAllowedForUrls]
"1"="https://*"
"2"="http://*"



;导入Chrome Flash优化设置 ，请注意注册表路径与Chromium不一样，chrome导入到MACHINE根键下面，并且子路径也与Chromium不同

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome]
"AllowOutdatedPlugins"=dword:00000001
"RunAllFlashInAllowMode"=dword:00000001
"DefaultPluginsSetting"=dword:00000001
"HardwareAccelerationModeEnabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\PluginsAllowedForUrls]
"1"="https://*"
"2"="http://*"
</pre>

<pre>
Windows Registry Editor Version 5.00

;删除Chromium FLASH设置
[HKEY_CURRENT_USER\SOFTWARE\Policies\Chromium]
"AllowOutdatedPlugins"=-
"RunAllFlashInAllowMode"=-
"DefaultPluginsSetting"=-
"HardwareAccelerationModeEnabled"=-

[HKEY_CURRENT_USER\SOFTWARE\Policies\Chromium\PluginsAllowedForUrls]
"1"=-
"2"=-

;删除Chrome FLASH设置
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome]
"AllowOutdatedPlugins"=-
"RunAllFlashInAllowMode"=-
"DefaultPluginsSetting"=-
"HardwareAccelerationModeEnabled"=-

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\PluginsAllowedForUrls]
"1"=-
"2"=-</pre>

[HashTab](http://implbits.com/products/hashtab/)

[WIN10精简版m8dq](https://pan.baidu.com/s/1aJCR2iTNU3XOLFdmu0Zjlg#m8dq) [UUP](https://uup.rg-adguard.net)

## Useful Websites
* [MSDN,我告诉你](https://msdn.itellyou.cn/)

* [老殁|殁漂遥](https://www.laomoit.com/)


## Software List(Important to me)
1. 微软常用运行库([DirectX 修复工具](https://blog.csdn.net/vbcom/article/details/6962388)、DirectX9.0c End-User Runtimes、[Flash](https://www.flash.cn/))

2. [Annie](https://github.com/iawia002/annie/releases)

3. [W10数字许可激活C#版](https://www.52pojie.cn/thread-742884-1-1.html) [原版](https://www.nsaneforums.com/topic/315047-w10-digital-license-generation-v31-c-version-of-hwid-fork/)

4. [rufus](https://github.com/pbatard/rufus/releases)

5. [FFmpeg(Static ver.)](https://ffmpeg.zeranoe.com/builds/)

6. [旺信](https://alimarket.taobao.com/markets/qnww/portal-group/ww/download)

7. Groupy

8. [PotPlayer](https://t1.daumcdn.net/potplayer/PotPlayer/Version/Latest/PotPlayerSetup64.exe)

9. [Snipaste](https://www.snipaste.com/)

10. [SteamAchievementManager (Auto ver.)](https://github.com/gotkrypto76/SteamAchievementManager)

11. QQ

12. [WinSCP](https://winscp.net/eng/download.php)

13. [Termius](https://www.termius.com/windows)

14. Office

15. [Adobe software series](https://weibo.com/vposy)

16. [Steam](https://store.steampowered.com/about/)

17. [Uplay](http://uplay.ubi.com/index.html)

18. [火绒](https://www.huorong.cn/downloadv5.html)

19. [Logitech Gaming Software](https://support.logitech.com.cn/zh_cn/downloads)

20. Fences

21. Start10

22. [Bandizip](http://www.bandisoft.com/bandizip/)

23. [Honeyview](http://www.bandisoft.com/honeyview/)

24. [JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html)

25. [GeForce Experience](https://www.nvidia.com/zh-cn/geforce/geforce-experience/)

26. [115](http://115.com/)

27. [小丸工具箱](https://maruko.appinn.me/)

28. [K-Lite Codec Pack Mega](http://www.codecguide.com/download_kl.htm)

29. [Chrome](https://www.google.com/intl/zh-CN/chrome/browser/thankyou.html?platform=win64&standalone=1&statcb=1&installdataindex=defaultbrowser) [企业版](https://cloud.google.com/chrome-enterprise/browser/download/)

30. [搜狗输入法](https://pinyin.sogou.com/)

31. [网易云音乐](https://music.163.com/#/download)

32. [MuMu模拟器](http://mumu.163.com/)

33. Newsflow(UWP)

34. [迅雷](http://x.xunlei.com/)

35. [TrafficMonitor](https://github.com/zhongyang219/TrafficMonitor/releases)

36. [VScode](https://code.visualstudio.com/)

37. [ScreenToGif](https://github.com/NickeManarin/ScreenToGif/releases)


## Software List(Optional)
1. [DISM++](http://www.chuyu.me/zh-Hans/index.html)

2. [Cheat Engine](https://cheatengine.org/)

3. [waifu2x-caffe](https://github.com/lltcggie/waifu2x-caffe) [cuDNN](https://developer.nvidia.com/rdp/cudnn-download)

4. Bandicam

5. Eclipse

6. [Telegram](https://telegram.org/apps)

7. Visual Studio

8. [Open Broadcaster Software](https://obsproject.com/download)

9. [Gifcam](http://blog.bahraniapps.com/gifcam/#download)

10.  [KMS Tools](https://www.solidfiles.com/folder/bd7165a0d4/)

11. 


## 美化软件

网址：[致美化](zhutix.com)

[noMeiryoUI](http://tatsu.life.coocan.jp/MySoft/index.html)

[MacType](https://www.mactype.net/)

[UltraUXThemePatcher](https://www.syssel.net/hoefs/software_uxtheme.php?lang=en)

[OldNewExplorerCfg](http://tihiy.net/files/OldNewExplorer.rar)
