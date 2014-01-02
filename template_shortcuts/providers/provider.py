class CDNProvider(object):
    base_url = NotImplemented

    def _build_url(self, lib_name, version, file_name=None):
        if file_name is None:
            file_name = lib_name
        return self.base_url % (lib_name, version, file_name)

    def _build_js_url(self, lib_name, version, file_name=None):
        url = self._build_url(lib_name, version, file_name)
        return "%s.min.js" % url

    def _build_css_url(self, lib_name, version, file_name=None):
        url = self._build_url(lib_name, version, file_name)
        return "%s.css" % url

    def angular(self, version):
        raise NotImplementedError()

    def jquery(self, version):
        raise NotImplementedError()

    def modernizr(self, version):
        raise NotImplementedError()

    def chrome_frame(self, version):
        raise NotImplementedError()

    def dojo(self, version):
        raise NotImplementedError()

    def ext_core(self, version):
        raise NotImplementedError()

    def jquery_ui(self, version):
        raise NotImplementedError()

    def mootools(self, version):
        raise NotImplementedError()

    def prototype(self, version):
        raise NotImplementedError()

    def scriptaculos(self, version):
        raise NotImplementedError()

    def swfobject(self, version):
        raise NotImplementedError()

    def webfont(self, version):
        raise NotImplementedError()
