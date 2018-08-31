
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_config(host):
    with host.sudo():
        fc = fr = None
        if host.system_info.distribution.lower() in debian_os:
            fc = host.file('/etc/powerdns/recursor.conf')
        if host.system_info.distribution.lower() in rhel_os:
            fc = host.file('/etc/pdns-recursor/recursor.conf')

        assert fc.exists
        assert 'threads=1' in fc.content
