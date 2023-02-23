"This is a .vimrc file made to configure some basic settings of vim. This can be
"useful for anyone programming with VIM. Please save this file in your home
"directory. You can use the following command to copy this file to your home
"directory (assuming you are in the directory where the .vimrc file is located):
"cp ./.vimrc ~

"This turns syntax highlighting on
syntax on

"The following command will make your *TAB* key converted to 4 spaces instead
"when editing file.
set tabstop=4
set shiftwidth=4
set expandtab

"This shows the line number when you edit file with VIM.
set number

"This draw a straight line after certain amount of characters in a row. This can give
"you an indication if your code is too long within the same row.
set colorcolumn=80

"When you learn about makefile in week 2. You will start writing your first
"makefile. Keep in mind that indentation with *TAB* key in makefile is compulsory to make it
"work. Since we had enabled the setting to convert TAB to 4 spaces, we need to
"add a rule exception when dealing with makefile.
autocmd FileType make setlocal noexpandtab

"Enable mouse support
set mouse=a

"set up debugger
let g:termdebug_wide=1
packadd termdebug