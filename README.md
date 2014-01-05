This git repository contains some experiments in making use of Wikidata via Lua
scripts.

# tl;dr

MediaWiki supports Lua to make use of content from Wikidata but existing Lua
scripts are not subject to serious software development.

# Lua support in MediaWiki

[Scribunto](https://www.mediawiki.org/wiki/Extension:Scribunto) is an extension
to embed Lua scripts in MediaWiki, the software that Wikipedia and other wikis
run with. The scripts are stored as "modules" in form of wiki pages in the
special *module*-namespace of a MediaWiki instance. Each module provides a set
of functions which can be called with optional arguments from other wiki pages.

    {{#invoke: Module_name | function_name | arg1 | arg2 | arg3 ... }}

To give an example ...

    ... TODO

The predefined table `mw` provides [additional Scribunto libraries](https://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual#Scribunto_libraries), for instance to load data and code from one module into another module.

There is a small [tutorial on Lua for MediaWiki](https://www.mediawiki.org/wiki/Lua_scripting/Tutorial).

# Scribuntu's console API

If a Lua script is not something huge, doesn't require (m)any external
dependencies, and doesn't have user interaction, one can make use of
Scribunto's console AJAX interface:

    ./consoleapi.py https://en.wikipedia.org/w/api.php < example.lua

# Local MediaWiki and Wikidata libraries

Local lua libraries to access MediaWiki and Wikidata do not exist yet. One
should create *Lua rocks* to access MediaWiki in general and WikiData in
particular.

# Managing Lua modules from MediaWiki in git

Managing program code in form of pages in a wiki is possible, but a pain compared to files in a source control system. Luckily there is [git-remote-mediawiki](https://github.com/moy/Git-Mediawiki/wiki), a bridge between MediaWiki and git.

    git init
    git remote add origin mediawiki::http://en.wikipedia.org/w/
    git -c remote.origin.pages=module:Hello pull
    ...

Fetching all pages in the module-namespace is [not supported yet](https://github.com/moy/Git-Mediawiki/issues/10).

# Managing Lua modules as Lua rocks

If source code is created to be used as programming library by other scripts,
putting it into a revision control system is only one part of serious software
development. The library or module should also be covered by documentation and
unit tests, and it should be distributed as software packaged. In the case of
Lua, the standard package management system is [Lua rocks](http://luarocks.org).

Until now there seems to exist no serious coordination of Lua scripts and
modules for MediaWiki in form of lua rocks. The Wikimedia habbit of just
managing everything in form of wiki pages makes serious management of Lua 
modules difficult but not impossible.

