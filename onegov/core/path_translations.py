from morepath.traject import parse_path
from pygtrie import StringTrie


class PathTranslations(object):

    def __init__(self):
        self.incoming = StringTrie()
        self.outgoing = {}

    def __bool__(self):
        return bool(self.incoming)

    def limit_to_static_part(self, path):
        position = path.find('{')

        if position > 0:
            return path[:position]

        return path

    def add_path_translations(self, path, translations):
        for locale, translation in translations.items():
            self.add_path(locale, path, translation)

    def add_path(self, locale, original, translated):
        if original == translated:
            return

        locale = locale[:2]

        if locale not in self.outgoing:
            self.outgoing[locale] = StringTrie()

        original = self.limit_to_static_part(original).strip('/')
        translated = self.limit_to_static_part(translated).strip('/')

        assert translated.count('/') == original.count('/')
        assert not self.incoming.has_node(translated)
        assert not self.outgoing[locale].has_node(original)

        self.incoming[translated] = original
        self.outgoing[locale][original] = translated

    def transform_incoming_request(self, request):
        path = request.path_info.strip('/')

        prefix, replacement = self.incoming.longest_prefix(path)

        if prefix and replacement:
            path = replacement + '/' + path[len(prefix):]

            request.path_info = path
            request.unconsumed = parse_path(path)
            request.unconsumed.reverse()

    def translate_outgoing_path(self, locale, path):
        locale = locale[:2]

        if locale not in self.outgoing:
            return path

        if '?' in path:
            path, suffix = path.split('?', 1)
        else:
            suffix = None

        path = path.strip('/')
        prefix, replacement = self.outgoing[locale].longest_prefix(path)

        if prefix and replacement:
            path = replacement + path[len(prefix):]

        if suffix:
            path += '?' + suffix

        return '/' + path
