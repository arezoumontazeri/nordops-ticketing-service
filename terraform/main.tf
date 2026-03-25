resource "aws_instance" "ticketing_server" {
  ami           = "ami-0c1ac8a41498c1a9c" # Ubuntu (eu-north-1)
  instance_type = "t3.micro"
  key_name = aws_key_pair.deployer.key_name

  vpc_security_group_ids = [
    aws_security_group.ticketing_sg.id
  ]

  tags = {
    Name = "ticketing-server"
  }
}
