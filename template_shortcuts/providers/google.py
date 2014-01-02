from provider import CDNProvider


class Google(CDNProvider):
    base_url = "//ajax.googleapis.com/ajax/libs/%s/%s/%s"

    def angular(self, version):
        return self._build_js_url("angularjs", version, "angular")

    def chrome_frame(self, version):
        return self._build_js_url("chrome-frame", version, "CFInstall")

    def jquery(self, version):
        return self._build_js_url("jquery", version)

    def ext_core(self, version):
        return self._build_js_url("ext-core", version)

    def jquery_ui(self, version):
        return self._build_js_url("jqueryui", version, "jquery-ui")

    def mootools(self, version):
        return self._build_js_url("mootools", version,
                                  "mootools-yui-compressed.js")

    def prototype(self, version):
        return self._build_js_url("prototype", version)

    def scriptaculos(self, version):
        return self._build_js_url("scriptaculos", version)

    def swfobject(self, version):
        return self._build_js_url("swfobject", version)

    def webfont(self, version):
        return self._build_js_url("webfont", version)
