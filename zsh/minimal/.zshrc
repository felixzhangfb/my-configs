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
alias sss="export {HTTP,HTTPS}_PROXY=http://127.0.0.1:1087;export NO_PROXY=localhost,127.0.0.1,::1"
alias uss="unset {HTTP,HTTPS,NO}_PROXY"
