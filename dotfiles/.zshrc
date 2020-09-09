# Personal preferences
unsetopt correct_all # spelling correction for arguments
setopt correct # spelling correction for commands
setopt complete_in_word # Allow completion from within a word/phrase
setopt list_ambiguous
setopt always_to_end # When completing from the middle of a word, move the cursor to the end of the word    
setopt hist_ignore_all_dups
setopt hist_no_store
setopt hist_reduce_blanks # Remove extra blanks from each command line being added to history
setopt hist_ignore_space # remove command line from history list when first character on the line is a space
setopt inc_append_history # Add comamnds as they are typed, don't wait until shell exit
setopt share_history # imports new commands and appends typed commands to history
setopt append_history # Allow multiple terminal sessions to all append to one zsh command history
setopt auto_cd # If you type foo, and it isn't a command, and it is a directory in your cdpath, go there
setopt hup
setopt complete_aliases
setopt auto_list
setopt no_beep # don't beep on error

# Aliases
alias poweroff='sudo shutdown -h now'
alias rsync='rsync -avzhP'
# alias cask='brew cask'
# alias bupdate='bubo && cask upgrade $(cask list) &&  bubc'

plugins=(sudo adb zsh-autosuggestions)
# plugins=(brew osx sudo adb zsh-autosuggestions)

# Exports
export GIT_HOME_DIR="~/Git/"
export LANG=en_US.UTF-8
export MANPATH="/usr/local/man:$MANPATH"
export EDITOR=$(which vim)
export HOSTNAME=$(cat /etc/hostname)
export TERM=xterm-256color
export SCRIPT=
# export ADB_SYNC_DEST="/Volumes/CROCCANTE/OnePlus"
# export HOMEBREW_CASK_OPTS="--appdir=/Applications"
# export SDKROOT=macosx10.14

# PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export PATH=$PATH

# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh
export ZSH_THEME="powerlevel10k/powerlevel10k"

source $ZSH/oh-my-zsh.sh
autoload -Uz compinit && compinit

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
