from provider import CDNProvider


class CDNJS(CDNProvider):
    base_url = "//cdnjs.cloudflare.com/ajax/libs/%s/%s/%s"

    def angular(self, version):
        return self._build_js_url("angular.js", version, "angular")

    def chrome_frame(self, version):
        return self._build_js_url("chrome-frame", version, "CFInstall")

    def modernizr(self, version):
        return self._build_js_url("modernizr", version)

    def jquery(self, version):
        return self._build_js_url("jquery", version)

    def ext_core(self, version):
        return self._build_js_url("ext-core", version)

    def jquery_ui(self, version):
        return self._build_js_url("jqueryui", version, "jquery-ui")

    def mootools(self, version):
        return self._build_js_url("mootools", version,
                                  "mootools-core-full-compat-yc")
