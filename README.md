This git repository contains some experiments in accessing Wikidata via Lua
scripts.

# Lua in MediaWiki

MediaWiki, the software that Wikipedia and other wikis run at, includes an
[extension called Scribunto](https://www.mediawiki.org/wiki/Extension:Scribunto).
This extension allows to add custom programming libraries in the Lua programming language.
These libraries are stored in the special *module*-namespace of a wiki. Each
module provides a set of functions (as Lua table), which can be called from
other wiki pages with the following syntax:

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

Local lua libraries to access MediaWiki and Wikidata do not exist yet.

# Managing Lua-MediaWiki-Modules in git

Managing program code in form of pages in a wiki is possible, but a pain compared to files in a source control system. Luckily there is [git-remote-mediawiki](https://github.com/moy/Git-Mediawiki/wiki), a bridge between MediaWiki and git.

    git init
    git remote add origin mediawiki::http://en.wikipedia.org/w/
    git -c remote.origin.pages=module:Hello pull
    ...

Fetching all pages in the module-namespace is [not supported yet](https://github.com/moy/Git-Mediawiki/issues/10).

