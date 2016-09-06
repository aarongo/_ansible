# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Use the same key for each machine
  config.ssh.insert_key = false

  # config.vm.define "vagrant1" do |vagrant1|
  #   vagrant1.vm.box = "centos65-x86_64"
  #   vagrant1.vm.hostname = "example001.nginx-node1.com"
  #   vagrant1.vm.box_check_update = false
  #   vagrant1.vm.network "forwarded_port", guest: 80, host: 8080
  #   config.vm.network "private_network", ip: "192.168.1.110"
  # end
  # config.vm.define "vagrant2" do |vagrant2|
  #   vagrant2.vm.box = "centos65-x86_64"
  #   vagrant2.vm.hostname = "example002.nginx-node1.com"
  #   vagrant2.vm.box_check_update = false
  #   vagrant2.vm.network "forwarded_port", guest: 80, host: 8081
  #   config.vm.network "private_network", ip: "192.168.1.111"
  # end
  config.vm.define "vagrant3" do |vagrant3|
    vagrant3.vm.box = "centos65-x86_64"
    vagrant3.vm.hostname = "example003.nginx-node1.com"
    vagrant3.vm.box_check_update = false
    vagrant3.vm.network "forwarded_port", guest: 80, host: 8082
    config.vm.network "private_network", ip: "192.168.1.112"
  end
end