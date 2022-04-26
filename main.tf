terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "dpalist_vm" {
  ami                    = "ami-04505e74c0741db8d"
  instance_type          = "t2.micro"
  key_name               = "dpalist1"
  vpc_security_group_ids = ["sg-0433c6a8b20f96b18"]

  user_data = <<EOF
#!/bin/bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install -y docker-ce
sudo chmod 666 /var/run/docker.sock
docker pull zubgkaow29cuto/dpalist
docker run -d -p 3000:3000 zubgkaow29cuto/dpalist
  EOF

  tags                   = { "Name" : "dpalist_vm" }
}
