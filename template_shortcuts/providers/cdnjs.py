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

    def angular(version):
        raise NotImplementedError()

    def jquery(version):
        raise NotImplementedError()

    def modernizr(version):
        raise NotImplementedError()


class CDNJS(CDNProvider):
    base_url = "//cdnjs.cloudflare.com/ajax/libs/%s/%s/%s"

    def angular(self, version):
        return self._build_js_url("angular", version)

    def jquery(self, version):
        return self._build_js_url("jquery", version)

    def modernizr(self, version):
        return self._build_js_url("modernizr", version)
