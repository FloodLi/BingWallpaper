# BingWallpaper
Auto change wallpaper for mac

定时更换：</br>
对应修改好.sh和plist文件的路径后</br>
将plist文件放入~/Library/LaunchAgents（由用户自己定义的任务项，推荐）</br>
launchctl的使用：</br>
添加 launchctl load ~/Library/LaunchAgents/com.AutoWallpaper.plist</br>
移除 launchctl unload ~/Library/LaunchAgents/com.AutoWallpaper.plist</br>
查看 launchctl list</br>

plist默认每天12：00自动更换壁纸
