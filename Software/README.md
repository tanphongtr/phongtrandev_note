# MacOS
### multipass
> https://multipass.run/  
> Máy ảo Ubuntu

### AppCleaner
> https://freemacsoft.net/appcleaner/  
![image](https://github.com/tanphongtr/phongtrandev_note/assets/11567406/3f6ef172-9591-4d09-8bbe-87592bbcc373)

### The Unarchiver
> https://theunarchiver.com/

### Fig
> https://fig.io/

### Hyper
> https://hyper.is/

### TG Pro
> https://www.tunabellysoftware.com/tgpro/

### Rectangle
> https://rectangleapp.com/  
> Move and resize windows in macOS using keyboard shortcuts or snap areas

### OrbStack
> https://orbstack.dev/  

### Terminus
> https://termius.com/download/macos  

### Background Music
> https://github.com/kyleneideck/BackgroundMusic  

### NextDns
> https://nextdns.io/  

### ProtonVPN
> https://protonvpn.com/  

### Cloudflare WARP
> https://1.1.1.1/  

### Warp
> https://www.warp.dev/  

### Cursor
> https://www.cursor.so/  

### Disk Drill
> https://www.disk-drill.com/

### PlayCover
> https://playcover.io/  
> https://decrypt.day/

### Clipy
> https://github.com/Clipy/Clipy

# Development

### Powerlevel10k
> https://github.com/romkatv/powerlevel10k

### Nodejs
```curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash```

Downloading nvm from git to '/Users/phongtran/.nvm'

```nvm install --lts```

### Pyenv

```
brew update
brew install pyenv

// For zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

pyenv install 3.10
pyenv global 3.10

// nếu install python version bị lỗi
brew install openssl readline sqlite3 xz zlib tcl-tk

python3 --version
> Python 3.10

```

### wrk

### Nodejs Env

### WireShark

### mitmproxy
```
brew install mitmproxy

mitmweb

// ssl
sudo security add-trusted-cert -d -p ssl -p basic -k /Library/Keychains/System.keychain ~/.mitmproxy/mitmproxy-ca-cert.pem
```
![image](https://github.com/tanphongtr/phongtrandev_note/assets/11567406/57a7df90-7a6d-49e6-b885-906cda1f963c)



# Ubuntu
### xrdp
```
$ sudo apt-get update
$ sudo apt-get install xrdp
```
> Remote Desktop Linux
