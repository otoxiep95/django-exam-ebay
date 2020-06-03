Vagrant.configure("2") do |config|
   config.vm.box = "mayocream/alpine-311"
   config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"
   config.vm.synced_folder ".", "/project", owner: "vagrant", group: "vagrant"

   config.vm.provision "shell", inline: <<-SHELL
      sudo apk add redis
      sudo apk add python3
      python3 -m venv django
      if [ -e /project/requirements.txt ]
      then
         . django/bin/activate
         pip install --upgrade pip
         pip install -r /project/requirements.txt
      fi
   SHELL
end