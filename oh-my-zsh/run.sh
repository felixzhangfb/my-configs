#!/bin/sh
ZSHRC="$HOME/.zshrc"
THEME='myagnoster'

cp custom/themes/"${THEME}.zsh-theme" ~/.oh-my-zsh/custom/themes/

if grep -q '^#*\s*ZSH_THEME=' "$ZSHRC"; then
  sed -i '' -E "s|^#*\s*ZSH_THEME=.*|ZSH_THEME=\"${THEME}\"|" "$ZSHRC"
fi