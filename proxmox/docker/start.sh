docker container stop ansible
docker run --rm -d -p 2020:22 --name ansible ansible
ansible-playbook playbook.yaml
