import sublime
import sublime_plugin
import webbrowser


class LeoCommand(sublime_plugin.TextCommand):
  def is_enabled(self):
    return True

  def doit(self, url):
    for region in self.view.sel():
      if region.begin() == region.end():
        word = self.view.word(region)
      else:
        word = region
      if not word.empty():
        keyword = self.view.substr(word)
        view = sublime.active_window().active_view()
        sel = view.sel()
        region1 = sel[0]
        selectionText = view.substr(region1)
        url = url + keyword
        webbrowser.open(url)


class LeoEnDeCommand(LeoCommand):
  def run(self, edit, **args):
    self.doit('http://dict.leo.org/ende/index_en.html#/search=')


class LeoDeEnCommand(LeoCommand):
  def run(self, edit, **args):
    self.doit('http://dict.leo.org/ende/index_en.html#/search=')
