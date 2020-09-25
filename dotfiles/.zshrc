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
export SAVEHIST=10000
export HISTSIZE=50000
export HISTFILE=$HOME/.zsh_history

# Aliases
alias poweroff='sudo shutdown -h now'
alias rsync='rsync -avzhP'

# Exports
export LANG=en_US.UTF-8
export MANPATH="/usr/local/man:$MANPATH"
export TERM=xterm-256color
export ZSH_PLUGINS=$HOME/.zsh-plugins

# env
source $ZSH_PLUGINS/env.zsh

# PATH
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
PATH=$PATH:$SCRIPT/python

# MacOS
if [[ "$(uname)" == "Darwin" ]]; then
    source $ZSH_PLUGINS/darwin.zsh
    export PATH=$PATH:/usr/local/bin/my:$SCRIPT/mac
else
    export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=23'
    export PATH=$PATH:$SCRIPT/bash
fi

# sudo
source $ZSH_PLUGINS/sudo/sudo.plugin.zsh
# zsh-autosuggestions
source $ZSH_PLUGINS/zsh-autosuggestions/zsh-autosuggestions.zsh
# powerlevel10k
source $ZSH_PLUGINS/powerlevel10k/powerlevel10k.zsh-theme
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
# compdump once a day
autoload -Uz compinit 
if [[ -n $HOME/.zcompdump(#qN.mh+24) ]]; then
	compinit
else
	compinit -C
fi
