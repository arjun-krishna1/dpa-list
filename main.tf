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
  tags                   = { "Name" : "dpalist_vm" }
}
