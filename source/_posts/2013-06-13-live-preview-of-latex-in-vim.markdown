---
layout: post
title: "Live Preview of LaTeX in Vim"
date: 2013-06-13T00:35:56
comments: true
external-url: 
categories: [LaTeX, Vim]
---

[Vim][], as a highly configurable and customizable editor, already has a powerful [Vim-LaTeX][] plugin. However, I don't
like the lack of live preview feature. For this reason, I developed a plugin called [vim-latex-live-preview][] last
year. Although it currently can't handle complex situations such as multiple tex files, it could basically handle single
tex file project well (with or without BibLaTeX, thanks to [Asis Hallab](https://github.com/asishallab)).

_Note: This plugin currently doesn't work on Windows._

<!-- more -->

## Installation

Before installing this plugin, please make sure that you have **++python** feature in your Vim. Type `:version` and if
you see `+python` in the output, then you have this feature enabled in your Vim. Then, you could either:

- drop [latexlivepreview.vim](http://github.com/xuhdev/vim-latex-live-preview/raw/master/plugin/latexlivepreview.vim)
into your `~/.vim/plugin` directory,
- or use Vim [pathogen][] plugin to install vim-latex-live-preview from its [git repository][vim-latex-live-preview].

I would recommend using the second way, since pathogen can well organize your installed plugin, making plugin
installation and uninstallation much easier.

## Usage

First please set the vim option `updatetime` to a smaller value, which is the frequency that the output PDF is updated.
I would recommend setting it to `1`. Basically you can simply add the following line to your `.vimrc` file:

```vim
autocmd Filetype tex setl updatetime=1
```

Then visit [this page](https://github.com/xuhdev/vim-latex-live-preview/wiki/Known-Working-PDF-Viewers) to see a list of
PDF viewers that could work with this plugin. If you want to use any pdf viewers that are not marked as "built-in", you
need to add the following line to your `.vimrc` file:

```vim
let g:livepreview_previewer = 'my_pdf_viewer'
```

Now open up a tex file with Vim. Run `:LLPStartPreview` to start previewing and enjoy!

If you frequently need to use the preview feature, I suggest you to map the preview command onto some key binding:

```vim
nmap <F12> :LLPStartPreview<cr>
```

## Screenshot

A simple screenshot:

![](http://github.com/xuhdev/vim-latex-live-preview/raw/master/screenshots/screenshot-evince.gif)

## An Alternative

An alternative might be [Kevin Klement's vim-live-latex-preview](https://github.com/ying17zi/vim-live-latex-preview),
which I haven't tried out though.


[Vim-LaTeX]: http://vim-latex.sourceforge.net/
[Vim]: http://www.vim.org
[pathogen]: http://www.vim.org/scripts/script.php?script_id=2332
[vim-latex-live-preview]: http://github.com/xuhdev/vim-latex-live-preview#readme
