#!/bin/sh

chsh -s $(which zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended --keep-zshrc

cp .zshrc $HOME
cp .p10k.zsh $HOME
cp .tmux.conf $HOME

git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $HOME/.oh-my-zsh/custom/themes/powerlevel10k
git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions

cd $HOME/.oh-my-zsh/custom/themes/powerlevel10k/internal
GIT_ICON_LINE=$(grep 'function _p9k_vcs_icon() {' p10k.zsh -n | awk -F ':' '{print $1}')
START_LINE=$(( $GIT_ICON_LINE + 1))
END_LINE=$(( $START_LINE + 6))
mv p10k.zsh p10k.zsh.tmp
sed $START_LINE','$END_LINE'd' p10k.zsh.tmp > p10k.zsh
cd $HOME

zsh