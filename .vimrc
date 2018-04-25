set number            " line 표시를 해줍니다.
"set ai                    " auto indent
"set si                    " smart indent
set ignorecase      " 검색시 대소문자 구별하지않음
set hlsearch         " 검색시 하이라이트(색상 강조)
set background=dark  " 검정배경을 사용할 때, (이 색상에 맞춰 문법 하이라이트 색상이 달라집니다.)
set nocompatible   " 방향키로 이동가능
set bs=indent,eol,start    " backspace 키 사용 가능
set history=1000    " 명령어에 대한 히스토리를 1000개까지
set ruler              " 상태표시줄에 커서의 위치 표시
set title               " 제목을 표시
set showmatch    " 매칭되는 괄호를 보여줌
set nowrap         " 자동 줄바꿈 하지 않음
set wmnu           " tab 자동완성시 가능한 목록을 보여줌
set nocindent
syntax on
nmap <F5> :split<CR>
nmap <F6> :vsplit<CR>
nmap <F7> :NERDTreeToggle<CR>

" Tab Handling
set tabstop=4
set softtabstop=4
"set expandtab
" Show line numbers
set number
" Show command in bottom bar
set showcmd
" Highlight the current line
set cursorline
"
" Visual autocomplete for command menu
set wildmenu
"
" " Redraw only when necessary, speeds up macros
set lazyredraw

filetype plugin on
let g:pydiction_location='/home/user/.vim/pydiction/complete-dict'

let python_version_2 = 1 " python 2 문법을 따른다고 옵션을 설정합니다.
let python_highlight_all = 1 " 모든 강조(색상) 기능을 켭니다.
language en_US.UTF-8
let g:Powerline_symbols = 'fancy'
set laststatus=2

set nocompatible              

set rtp+=/home/user/.vim/bundle/Vundle.vim
" let Vundle manage Vundle
" " " required! 
" " " My bundles here:
"
filetype plugin indent on     " required!
