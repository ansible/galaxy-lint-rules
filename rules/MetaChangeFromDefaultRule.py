from ansiblelint import AnsibleLintRule


class MetaChangeFromDefaultRule(AnsibleLintRule):
    id = '703GAL'
    shortdesc = 'meta/main.yml default values should be changed'
    field_defaults = [
        ('author', 'your name'),
        ('description', 'your description'),
        ('company', 'your company (optional)'),
        ('license', 'your license'),
    ]
    description = ('meta/main.yml default values should be changed for: ' +
                   ', '.join([f[0] for f in field_defaults]))
    tags = ['metadata']

    def matchplay(self, file, data):
        if file['type'] != 'meta':
            return False

        galaxy_info = data.get('galaxy_info', None)
        if not galaxy_info:
            return False

        results = []
        for field, default in self.field_defaults:
            value = galaxy_info.get(field, None)
            if value and value == default:
                results.append(({'meta/main.yml': data},
                                'Should change default metadata: %s' % field))

        return results
