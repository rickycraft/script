# Mac zsh config

alias cask='brew cask'
alias bupdate='bubo && brew upgrade --cask $(brew list --cask) &&  bubc'

export GIT_HOME_DIR=$HOME/Git
export SCRIPT=$HOME/Git/script
export ADB_SYNC_DEST="/Volumes/CROCCANTE/OnePlus"
export HOMEBREW_CASK_OPTS="--appdir=/Applications"
export SDKROOT=macosx10.14

source $ZSH_PLUGINS/osx/osx.plugin.zsh
source $ZSH_PLUGINS/brew/brew.plugin.zsh
