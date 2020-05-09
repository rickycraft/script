#Personal preferences
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

#alias
alias bupdate='bubo && cask upgrade $(cask list) &&  bubc'
alias poweroff='sudo shutdown -h now'
alias rsync='rsync -avzhP'
alias cask='brew cask'

plugins=(brew osx extract web-search sudo adb fzf)

ZSH_THEME="riccardo"

#my new path
export PATH=/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet:/opt/X11/bin:/usr/local/bin/my

# Path to your oh-my-zsh installation.
export ZSH=/Users/rick/.oh-my-zsh

# MacOS Libraries
export SDKROOT=macosx10.14

#exports
export EDITOR="/usr/bin/nano"
export REPORTTIME=10
export HOMEBREW_CASK_OPTS="--appdir=/Applications"
export GIT_HOME_DIR="/Users/rick/Git/"

# User configuration
export MANPATH="/usr/local/man:$MANPATH"

#fzf
export FZF_BASE="/usr/local/bin/fzf"

# Uncomment the following line to disable fuzzy completion
# export DISABLE_FZF_AUTO_COMPLETION="true"

# Uncomment the following line to disable key bindings (CTRL-T, CTRL-R, ALT-C)
# export DISABLE_FZF_KEY_BINDINGS="true"

# You may need to manually set your language environment
export LANG=en_US.UTF-8

# ssh
export SSH_KEY_PATH="~/.ssh/rsa_id"

source $ZSH/oh-my-zsh.sh
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh

autoload -Uz compinit && compinit
