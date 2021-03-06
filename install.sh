#!/usr/bin/env sh
#

lscolors_data_dir="${XDG_DATA_HOME:-$HOME/.local/share}"
ranger_colorscheme_dir="$HOME/.config/ranger/colorschemes"

if dircolors -b LS_COLORS > lscolors.sh && dircolors -c LS_COLORS > lscolors.csh ; then
  if mv -t "$lscolors_data_dir" lscolors.sh lscolors.csh ; then
    cat <<EOF
To enable the colors, add the following line to your shell's start-up script:

For Bourne shell (e.g. ~/.bashrc or ~/.zshrc):
  . "$lscolors_data_dir/lscolors.sh"

For C shell (e.g. ~/.cshrc):
  . "$lscolors_data_dir/lscolors.csh"

EOF
  fi
fi

cp -v ranger/isene.py "$ranger_colorscheme_dir"
