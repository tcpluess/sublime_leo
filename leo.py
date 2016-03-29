import sublime
import sublime_plugin
import webbrowser


class LeoCommand(sublime_plugin.TextCommand):
  def is_enabled(self):
    view = sublime.active_window().active_view()
    return view.has_non_empty_selection_region()

  def doit(self, url):
    view = sublime.active_window().active_view()
    sel = view.sel()
    region1 = sel[0]
    selectionText = view.substr(region1)
    url = url + selectionText
    webbrowser.open(url)


class LeoEnDeCommand(LeoCommand):
  def run(self, edit, **args):
    self.doit('http://dict.leo.org/ende/index_en.html#/search=')


class LeoDeEnCommand(LeoCommand):
  def run(self, edit, **args):
    self.doit('http://dict.leo.org/ende/index_en.html#/search=')
