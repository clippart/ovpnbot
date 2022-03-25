import subprocess
import re

import paths


def update_template(usr):
    with open(paths.client_common, 'r') as i, \
            open(paths.ca_cert.format(user_id=usr), 'r') as cert, \
            open(paths.private_key.format(user_id=usr), 'r') as key, \
            open(paths.sertificat, 'w') as result:
        cert_text = cert.read()
        ca_cert = re.search(r'-----BEGIN CERTIFICATE-----(.*\n)*-----END CERTIFICATE-----', cert_text, re.M)[0]
        result.write(f'{i.read()}'
                     f'<ca>\n{cert.read()}</ca>'
                     f'\n<cert>\n{ca_cert}\n</cert>'
                     f'\n<key>\n{key.read()}</key>')
        return open(paths.sertificat, 'rb')


def gen_sert(user_id):
    subprocess.check_call('%s/easyrsa build-client_common-full %s nopass' % (paths.rsapath, user_id), shell=True, executable='/bin/bash')
    return update_template(user_id)


if __name__ == '__main__':
    gen_sert('43434343')
