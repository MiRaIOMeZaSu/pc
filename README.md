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

7. [FFmpegMininum.dll H.265/AAC音频解码器](http://get.daum.net/PotPlayer64/v4/Module/FFmpeg/FFmpegMininum64.dll)

8. [PotPlayer](http://t1.daumcdn.net/potplayer/beta/PotPlayerSetup.exe)

9. [Snipaste](https://www.snipaste.com/)

10. [SteamAchievementManager (Auto ver.)](https://github.com/gotkrypto76/SteamAchievementManager)

11. TIM

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

30. [搜狗输入法(智慧版)](https://pinyin.sogou.com/)

31. [网易云音乐](https://music.163.com/#/download)

32. [MuMu模拟器](http://mumu.163.com/)

33. Newsflow(UWP)

34. [迅雷](http://x.xunlei.com/)

35. [TrafficMonitor](https://github.com/zhongyang219/TrafficMonitor/releases)

36. [VScode](https://code.visualstudio.com/)

37. 


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
