config.load_autoconfig()

#config.set("colors.webpage.darkmode.enabled", True)

#swapforqute
sfq_base_dir = "~/.config/qutebrowser/userscripts/swapforqute/"
sfq_script_path = sfq_base_dir + "main.py"
sfq_conf_path = sfq_base_dir + "config.json"
sfq_cmd = "--userscript {} -c {}".format(sfq_script_path, sfq_conf_path)

c.aliases['sfq'] = "set-cmd-text -s :spawn {} --cmd 'open' -u ".format(sfq_cmd)
#config.bind('f', "hint links spawn {} --cmd 'open' -u ".format(sfq_cmd) + " {hint-url}")
#config.bind('F', "hint links spawn {} --cmd 'open -t' -u ".format(sfq_cmd) + " {hint-url}")


# Bindings
config.bind("<f2>", "inspector")
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind("xx", "config-cycle statusbar.show always never;; config-cycle tabs.show always never")
config.bind("pp", 'spawn xdotool key space ;; spawn --detach mpv {url}')
config.bind("wl", "spawn bash -c 'echo {url} >> ~/.config/qutebrowser/userscripts/watchLater.txt'")
config.bind("wr", "spawn bash -c 'grep -v {url} ~/.config/qutebrowser/userscripts/watchLater.txt >> tmp.txt && mv tmp.txt ~/.config/qutebrowser/userscripts/watchLater.txt'")
config.bind("wp", "spawn bash -c 'mpv $(~/.config/qutebrowser/userscripts/watchLater.sh)'")

# Search Engines
c.url.searchengines = \
    { "DEFAULT" : "https://search.inetol.net/search?q={}&category_general=1&language=all",\
     "w" : "http://en.wikipedia.org/w/index.php?search={}&title=Special:Search",\
     "y" : "http://www.youtube.com/results?search_query={}",\
     "d" : "http://dictionary.reference.com/browse/{}?s=t",\
     "g" : "https://www.google.com/search?q={}&source=web"
    }

#Colors
bg = "#1D252C"
lighterBg = "#42464C"
darkerBg = "#171D22"
fg = "#a0b3c5"
altFg = "#b62d65"
darkerFg = "#000"
lighterFg = "#FFF"
m_Splash3 = "#539AFC" 
m_Splash5 = "#A659B4"
m_Splash6 = "#70E1E8"
m_Splash7 = "#114B6A"

c.colors.statusbar.normal.bg = bg
c.colors.statusbar.command.bg = bg
c.colors.statusbar.normal.fg = fg
c.colors.statusbar.command.fg = fg
c.colors.statusbar.url.success.https.fg = fg
c.colors.tabs.even.bg = bg
c.colors.tabs.odd.bg = bg
c.colors.tabs.even.fg = fg
c.colors.tabs.odd.fg = fg
c.colors.tabs.selected.even.bg = m_Splash7
c.colors.tabs.selected.odd.bg = m_Splash7
c.colors.tabs.selected.even.fg = lighterFg
c.colors.tabs.selected.odd.fg = lighterFg
c.colors.tabs.indicator.stop = altFg
c.colors.completion.category.bg = darkerBg
c.colors.completion.category.fg = lighterFg
c.colors.completion.even.bg = bg
c.colors.completion.odd.bg = lighterBg
c.colors.completion.fg = fg
c.colors.completion.item.selected.bg = darkerBg
c.colors.completion.item.selected.fg = fg
c.colors.completion.match.fg = lighterFg
c.colors.downloads.bar.bg = lighterBg
c.colors.downloads.error.bg = lighterFg
c.colors.downloads.error.fg = darkerFg
c.colors.downloads.start.bg = m_Splash6
c.colors.downloads.start.fg = darkerFg
c.colors.downloads.stop.bg = darkerBg
c.colors.downloads.stop.fg = altFg

c.colors.hints.bg = m_Splash5
c.colors.hints.fg = darkerFg
c.colors.hints.match.fg = m_Splash3
c.hints.border = darkerFg

c.colors.keyhint.bg = m_Splash5
c.colors.keyhint.fg = darkerFg

c.colors.prompts.bg = darkerBg
c.colors.prompts.fg = altFg
