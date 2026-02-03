colorscheme default
filetype indent on
filetype plugin on
syntax enable

set autoindent
set background=dark
set backspace=indent,eol,start
set cindent
set cmdheight=2
" set cursorcolumn
" set cursorline
" set cursorlineopt=screenline,number
set encoding=utf-8
set expandtab
set fileencoding=utf-8
set fileencodings=utf-8,usc-bom,utf-16,cp936,gb18030,big5,euc-jp,euc-kr,latin1
set fileformat=unix
set fileformats=unix,dos,mac
set foldcolumn=1
set foldmethod=indent
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set magic
set mouse=a
set nobackup
set nocompatible
set nofoldenable
set nolinebreak
set nowrap
set nowritebackup
set number
set paste
set regexpengine=0
set scrolloff=5
set shiftround
set shiftwidth=4
set showbreak=+++
set showcmd
set showmatch
set showmode
set showtabline=2
set sidescrolloff=5
set smartcase
set smartindent
set smarttab
set softtabstop=4
set statusline=%F%m%r%h%w%=%y\ %{&fileformat}\ %{&fileencoding?&fileencoding:&encoding}\ %l:%c\ %p%%
set t_Co=256
set tabstop=4
set termencoding=utf-8
set whichwrap+=<,>,h,l

inoremap <C-v> <ESC>"*pi
vnoremap <C-c> "*y
vnoremap <C-v> c<ESC>"*pv
