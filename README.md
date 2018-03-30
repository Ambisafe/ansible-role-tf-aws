Terraform deployment
=========

Ansible role that install ecs and rds onto aws through terraform

Example Playbook
----------------
requirements.yml

```
- name: terraform-aws
  src: https://github.com/Ambisafe/ansible-role-tf-aws.git
  version: master
```

playbook.yml

```
- name: testing role terraform-aws
  hosts: localhost
  gather_facts: false
  vars:
    project_name: "test"
    project_deployment_environment: "stage"

    aws_region : "eu-west-1"
    aws_vpc_default: "True"
    ecs_min_size: 0
    ecs_max_size: 1
    ecs_desired_capacity: 1
    ecs_instance_type: "t2.micro"
    ecs_block_device_size: 22
    ecs_ssh_public_key: "ssh-rsa XXXXXXXXXXXXXXXXXXX"

    db_instance_type: "db.t2.micro"
    db_engine: "mysql"
    db_engine_version: "5.6.37"
    db_allocated_storage_size: 10
    db_name: "XXXXXXXXXXXXX"
    db_username: "XXXXXXXXXXXX"
    db_password: "XXXXXXXXXXXXXXXXX"
    db_skip_final_snapshot: "true"

    terraform_data_dir: "/tmp/.tf"

    project_domain_zone: "google.com"

  roles:
    - { role: terraform-aws }
```

Author Information
------------------
Artem Yushkov

DevOps@Ambisafe
