# Interactive shells only

## Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

## Set name of the theme to load
ZSH_THEME="myagnoster"

## Activate omz
source $ZSH/oh-my-zsh.sh

## Activate zsh-autosuggestions
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

## Optimized Docker CLI and completions
case ":${PATH}:" in
    *:"/Applications/Docker.app/Contents/Resources/bin":*)
        ;;
    *)
        export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"
        ;;
esac
fpath=(/Users/zfb/.docker/completions $fpath)
autoload -Uz compinit
compinit
# End of Docker CLI completions


## Set custom aliases
alias l="ls -haliF"
### shadowsocks
alias sss="export {HTTP,HTTPS}_PROXY=http://127.0.0.1:1087;export NO_PROXY=localhost,127.0.0.1,::1"
alias uss="unset {HTTP,HTTPS,NO}_PROXY"
### global python alias
alias python=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
alias py=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
alias pip=/Library/Frameworks/Python.framework/Versions/3.14/bin/pip3


## Set postgres functions
start_pg() {
    /opt/homebrew/opt/postgresql@18/bin/pg_ctl \
        -D /opt/homebrew/var/postgresql@18 \
        -l /opt/homebrew/var/postgresql@18/server.log \
        start
}

stop_pg() {
    /opt/homebrew/opt/postgresql@18/bin/pg_ctl \
        -D /opt/homebrew/var/postgresql@18 \
        stop
}

status_pg() {
    /opt/homebrew/opt/postgresql@18/bin/pg_ctl \
        -D /opt/homebrew/var/postgresql@18 \
        status
}
