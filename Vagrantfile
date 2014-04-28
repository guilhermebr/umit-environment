# Umit Project Dev Enviroment
#
#
VAGRANTFILE_API_VERSION = "2"

box      = 'precise32'
url      = 'http://files.vagrantup.com/precise32.box'
hostname = 'umitdev'
domain   = 'umitproject.com'
ip       = '192.168.0.42'
ram      = '256'


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config| 
  config.vm.box = box
  config.vm.box_url = url
  config.vm.host_name = hostname + '.' + domain
  config.vm.network :private_network, ip: ip
  #config.vm.network :public_network
  config.vm.synced_folder "./projects/", "/home/vagrant/umit"

  config.ssh.forward_x11 = true

  config.vm.provider :virtualbox do |vb|
    vb.customize [
      'modifyvm', :id,
      '--name', hostname,
      '--memory', ram
    ]
  end

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = 'puppet/manifests'
    puppet.manifest_file = 'umit.pp'
    puppet.module_path = 'puppet/modules'
  end
end

