# BingWallpaper
Auto change wallpaper for mac

定时更换：
对应修改好.sh和plist文件的路径后
将plist文件放入~/Library/LaunchAgents（由用户自己定义的任务项，推荐）
launchctl的使用：
添加 launchctl load ~/Library/LaunchAgents/com.AutoWallpaper.plist
移除 launchctl unload ~/Library/LaunchAgents/com.AutoWallpaper.plist
查看 launchctl list

plist默认每天12：00自动更换壁纸
