# Personal_Software_List
避免每次装机重头寻找历史安装过的软件，索性列一个清单，炼成半小时装机软件复原大法

CPU核数设置:msconfig
卓越性能：
<pre>
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
</pre>
一键设置所有uwp应用使用代理（用cmd）：
<pre>
FOR /F "tokens=11 delims=\" %p IN ('REG QUERY "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings"') DO CheckNetIsolation.exe LoopbackExempt -a -p=%p
</pre>
git代理设置：
<pre>
# ssh代理设置文件路径：C:\Users\username\.ssh\config
Host github.com
ProxyCommand connect -S 127.0.0.1:2080 %h %p

# git只吃http代理，https会被无视，无需设置
# git config --global http.https://github.com.proxy socks5://127.0.0.1:2080
# http代理设置文件路径：C:\Users\username\.gitconfig
[http "https://github.com"]
	proxy = socks5://127.0.0.1:2080
</pre>
<pre>
Chrome浏览器实验性功能：
Override software rendering list
GPU rasterization
Out of process rasterization
Enable native notifications.
Parallel downloading
Tab Hover Card Images
Skia API for OOP-D compositing
</pre>

<pre>
Windows Registry Editor Version 5.00

;如需还原去除上语句前减号即可

;取消我的电脑"视频"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{f86fa3ab-70d2-4fc7-9c99-fcbf05467f3a}]

;取消我的电脑"文档"文件夹

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{d3162b92-9365-467a-956b-92703aca08af}]

;取消我的电脑"桌面"文件夹

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}]

;取消我的电脑"音乐"文件夹?

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{3dfdf296-dbec-4fb4-81d1-6a3438bcf4de}]

;取消我的电脑"下载"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{088e3905-0323-4b02-9826-5d99428e115f}]

;取消我的电脑"图片"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{24ad3ad4-a569-4530-98e1-ab02f9417aa8}]

;取消我的电脑"3D对象"文件夹

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\MyComputer\NameSpace\{0DB7E03F-FC29-4DC6-9020-FF41B59E513A}]
</pre>

<pre>
youtube-dl设置文件目录：C:\Users\user name\youtube-dl.conf
-i
--proxy socks5://127.0.0.1:2080/
-f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
-o V:/annie/"%(uploader)s (%(uploader_id)s)/%(upload_date)s - %(title)s - (%(duration)ss) [%(resolution)s] [%(id)s].%(ext)s"
--add-metadata
--write-description
--write-thumbnail
</pre>

<pre>
Windows Registry Editor Version 5.00

;导入Flash优化设置 支持Chromium/Chrome/新版Edge .

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



;导入新版Edge优化设置
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge]
"AllowOutdatedPlugins"=dword:00000001
"RunAllFlashInAllowMode"=dword:00000001
"DefaultPluginsSetting"=dword:00000001
"HardwareAccelerationModeEnabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\PluginsAllowedForUrls]
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
"2"=-

;删除新版Edge设置
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge]
"AllowOutdatedPlugins"=-
"RunAllFlashInAllowMode"=-
"DefaultPluginsSetting"=-
"HardwareAccelerationModeEnabled"=-

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\PluginsAllowedForUrls]
"1"=-
"2"=-
</pre>

<pre>
IntelliJ IDEA设置备忘录

【IntelliJ IDEA启动参数】
文件目录：~\JetBrains\IntelliJIDEA\bin\idea64.exe.vmoptions
-Xms2048m
-Xmx2048m
-XX:ReservedCodeCacheSize=1024m
【皮肤设置1】
Appearance & Behavior —— Appearance —— Theme：One Dark vivid 
【代理设置】
Appearance & Behavior —— System Settings —— HTTP Proxy —— Manual proxy configuration —— √ SOCKS ； Host name：127.0.0.1 ； Port number：2080 
【悬浮提示】
Editor —— General —— √ Show quick documentation on mouse move 
【取消单行显示标签页】
Editor —— General —— × Show tabs in one row 
【滚轮修改字体大小】
Editor —— General —— √ Change font size(Zoom) with Ctrl+Mouse Wheel 
【自动导包】
Editor —— General —— Auto Import —— Insert imports on paste：All ；√ AddUnambiguous imports on the fly ；√ Optimize imports on the fly（for current project） 
【设置行号显示】
Editor —— General —— Appearance —— √ Show line numbers ； √ Show method separators 
【忽略大小写】
Editor —— General —— Code Completion —— × Match case 
【字体】
Editor —— Font —— Font：JetBrains Mono ； Size：13 ； Line spacing：1 ； Fallback font：Microsoft YaHei UI 
【皮肤设置2】
Editor —— Color Scheme —— Scheme：One Dark vivid 
【自动换行】
Editor —— Code Style —— √ Wrap on typing ； —— Java —— √ Ensure right margin is not exceeded 
【单行注释斜杠跟着代码】
Editor —— Code Style —— Java —— Code Generation —— × Line comment at first column ； √ Add a space at comment start 
【项目文件编码】
Editor —— File Encodings —— Global Encoding：UTF-8 ； Project Encoding：UTF-8 ； Default encoding for properties files：UTF-8 ； √ Transparent native-to-ascii conversion 
【插件列表】
Plugins —— One Dark theme ； Rainbow Brackets ； Translation 
【自动编译项目】
Build, Execution, Deployment —— Compiler —— √ Build project automatically 
【增加堆内存】
Build, Execution, Deployment —— Compiler —— Build process heap size(Mbytes)：2048 
【翻译设置】
Other Settings —— Translation —— √ 覆盖默认字体(推荐) ； 主要字体：Microsoft YaHei UI ； 音标字体：Arial 
</pre>

## Useful Websites
* [UUP dump](https://uupdump.ml/?lang=zh-cn)

* [423Down](https://www.423down.com/)

* [果核剥壳](https://www.ghpym.com/)

* [远景论坛](http://bbs.pcbeta.com/forum-win10-1.html)

## Software List(Indispensable)
1. [微软常用运行库](https://github.com/abbodi1406/vcredist/releases)、    [DirectX修复工具增强版](https://blog.csdn.net/vbcom/article/details/7245186)、                [DirectX9.0c End-User Runtimes](https://www.microsoft.com/zh-CN/download/details.aspx?id=35)、    [Flash](https://www.423down.com/2082.html)

2. [youtube-dl](https://github.com/ytdl-org/youtube-dl/releases)    [Annie](https://github.com/iawia002/annie/releases)

3. [HWID_KMS38](http://bbs.pcbeta.com/viewthread-1811496-1-1.html)

4. [TrafficMonitor](https://github.com/zhongyang219/TrafficMonitor/releases)

5. [FFmpeg(Static ver.)](https://ffmpeg.zeranoe.com/builds/)

6. [旺信](https://alimarket.taobao.com/markets/qnww/portal-group/ww/download)

7. Groupy(Steam)

8. [PotPlayer](https://potplayer.daum.net/)

9. [Snipaste](https://www.snipaste.com/)

10. [SteamAchievementManager (Auto ver.)](https://github.com/gotkrypto76/SteamAchievementManager)

11. [QQ](https://im.qq.com/download/)    [NtrQQ](https://github.com/NtrQQ/download/releases)    [iYa.App 软件交流社区](https://iya.app/)

12. [WinSCP](https://winscp.net/eng/download.php)

13. [Termius](https://www.termius.com/windows)

14. [Office Tool Plus](https://github.com/YerongAI/Office-Tool/releases)

15. [Adobe software series](https://weibo.com/vposy)

16. [Steam](https://store.steampowered.com/about/)

17. [Uplay](http://uplay.ubi.com/index.html)

18. [火绒](https://www.huorong.cn/person5.html)

19. [Logitech Gaming Software](https://support.logitech.com.cn/zh_cn/downloads)

20. Fences(Steam)

21. Start10(Steam)

22. [Bandizip](https://www.bandisoft.com/bandizip/dl/)    [patch](https://www.423down.com/9735.html)    [7-Zip](https://www.7-zip.org/)

23. [Honeyview](http://www.bandisoft.com/honeyview/)    [qimgv](https://github.com/easymodo/qimgv/releases)

24. [JDK](https://www.oracle.com/java/technologies/javase-downloads.html)

25. [GeForce Experience](https://www.nvidia.com/zh-cn/geforce/geforce-experience/)

26. [迅雷](http://x.xunlei.com/)

27. [小丸工具箱](https://maruko.appinn.me/)    [XMedia Recode](https://www.xmedia-recode.de/en/download.php)

28. [K-Lite Codec Pack Mega](http://www.codecguide.com/download_kl.htm)

29. [Chrome](https://www.google.com/intl/zh-CN/chrome/browser/thankyou.html?platform=win64&standalone=1&statcb=1&installdataindex=defaultbrowser)

30. [搜狗输入法](https://pinyin.sogou.com/)

31. [网易云音乐](https://music.163.com/#/download)

32. [VScode](https://code.visualstudio.com/)

33. Newsflow(UWP)

34. [百度云](http://pan.baidu.com/download)

35. [酷Q](https://cqp.cc/t/23253)

36. [Discord](https://discordapp.com/download)

37. [Everything](https://www.voidtools.com/zh-cn/downloads/)

38. [YouTube Live Chat Flow](https://github.com/fiahfy/youtube-live-chat-flow/releases)

39. 热角(UWP)

40. [nvidiaProfileInspector](https://github.com/Orbmu2k/nvidiaProfileInspector/releases/)

41. [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows)    [JetBrains Mono](https://www.jetbrains.com/lp/mono/)    [patch](https://zhile.io/)

42. [CCleaner](https://www.423down.com/716.html)    [Winapp2](https://github.com/MoscaDotTo/Winapp2)

43. [OpenHashTab](https://github.com/namazso/OpenHashTab/releases)

44. [ScreenToGif](https://github.com/NickeManarin/ScreenToGif/releases)

45. 


## Software List(Optional)
1. [DISM++](http://www.chuyu.me/zh-Hans/index.html)

2. [Cheat Engine](https://cheatengine.org/)

3. [waifu2x-caffe](https://github.com/lltcggie/waifu2x-caffe)    [cuDNN](https://developer.nvidia.com/rdp/cudnn-download)    [Waifu2x-Extension-GUI](https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases)

4. [KMS Tools](https://www.solidfiles.com/folder/bd7165a0d4/)

5. [Open Broadcaster Software](https://obsproject.com/download)

6. [万兴系列软件](https://www.423down.com/9357.html)

7. [WinRAR](https://hrtsea.com/121.html)

8. [rufus](https://github.com/pbatard/rufus/releases)

9.  [UltraISO](https://www.423down.com/1397.html)

10. 


## 美化软件(Unstable)

[致美化](https://zhutix.com/)

[noMeiryoUI](http://tatsu.life.coocan.jp/MySoft/index.html)

[MacType](https://www.mactype.net/)

[UltraUXThemePatcher](https://www.syssel.net/hoefs/software_uxtheme.php?lang=en)

[OldNewExplorerCfg](https://tihiy.net/files/OldNewExplorer.rar)
