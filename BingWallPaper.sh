curl -o ~/Library/Caches/bing.zip https://codeload.github.com/phidiascheng/bingWallPaper/zip/master 
unzip ~/Library/Caches/bing.zip -d ~/Library/Caches
/usr/local/bin/python3 ~/Library/Caches/bingWallPaper-master/bing.py
rm -f ~/Library/Caches/bing.zip
rm -rf ~/Library/Caches/bingWallPaper-master