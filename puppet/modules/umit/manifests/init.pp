class umit {

  $packs2 = [ "git", "build-essential", "libtool", "vim", "python-setuptools", "python-dev", "python-pip", "python-virtualenv" ]
  package { 
    $packs2: ensure => present,
  #  before => File['/home/vagrant/umit/install.sh'],
  }

  $packs = [ "libpcap-dev", "gtk+2", "libgtk2.0-dev", "nmap", "libgtkhex-3-dev" ]
  package { 
    $packs: ensure => present,
  #  before => File['/home/vagrant/umit/install.sh'],
  }

  exec { 'update-alternatives  --set editor /usr/bin/vim.basic':
    command => '/usr/bin/update-alternatives --set editor /usr/bin/vim.basic',
    require => Package['vim'],

  }

  #file {
  #  '/home/vagrant/umit/install.sh':
  #    owner => 'vagrant',
  #    group => 'vagrant',
  #    mode  => '0644',
  #    source => 'puppet:///modules/umit/install.sh',
  #}

  #exec { 'sh /home/vagrant/umit/install.sh':
  #  command => '/bin/bash /home/vagrant/umit/install.sh',
  #  require  => File['/home/vagrant/umit/install.sh'],
  #}
}