from ansiblelint import AnsibleLintRule
import os
import json


class MetaLicenseValidRule(AnsibleLintRule):
    id = '704GAL'
    shortdesc = "Expected 'license' to be a valid SPDX license ID"
    description = ("Expected 'license' to be a valid SPDX license ID."
                   "Valid licenses IDs can be found at https://spdx.org")
    tags = ['metadata']

    def matchplay(self, file, data):
        if file['type'] != 'meta':
            return False

        galaxy_info = data.get('galaxy_info', None)
        if not galaxy_info:
            return False

        role_license = galaxy_info.get('license', None)
        if not role_license:
            return False

        # spdx_licenses.json retrieved from:
        # https://github.com/spdx/license-list-data/blob/master/json/
        # licenses.json

        cwd = os.path.dirname(os.path.abspath(__file__))
        license_path = os.path.join(cwd, 'spdx_licenses.json')
        spdx_licenses = json.load(open(license_path, 'r'))
        for valid_license in spdx_licenses['licenses']:
            if valid_license['licenseId'] == role_license:
                if not valid_license['isDeprecatedLicenseId']:
                    return False

        msg = ("Expected 'license' to be a valid SPDX license ID, "
               "instead found '%s'. "
               "For more info, visit https://spdx.org" % role_license)
        return ({'meta/main.yml': data}, msg)
