resource "aws_instance" "ticketing_server" {
  ami           = "ami-0c1ac8a41498c1a9c"
  instance_type = "t3.micro"

  key_name  = aws_key_pair.deployer.key_name
  subnet_id = aws_subnet.public.id

  vpc_security_group_ids = [
    aws_security_group.ticketing_sg.id
  ]

  tags = {
    Name = "ticketing-server"
  }
}
