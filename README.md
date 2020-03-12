# Flaskr

Flaskr is a classic Python template (based on [the Flask framework](https://github.com/pallets/flask)) to quickly create complete web application. Included [Vagrant](https://github.com/hashicorp/vagrant) and [Docker](https://github.com/docker/docker-install) makes to configure the deployment environment in a flexible way.

### Integration

- [Gunicorn](https://github.com/benoitc/gunicorn)
- [PostgreSQL](https://github.com/postgres/postgres)
- [UIkit](https://github.com/uikit/uikit)

### Installation

- Clone the repository, copy `.env.example` to `.env` and `docker/.env.example` to `docker/.env` and modify them as you wish. You can also edit `docker/docker-compose.yml` if necessary.
- Execute the command `vagrant up`.
- For authorization, use the next bunch of username/password: `admin/admin`.

### Tests

- `$ sudo docker-compose run --rm -w /home python python3 -m unittest -v flaskr.tests.functional.test_blog`
- `$ sudo docker-compose run --rm -w /home python python3 -m unittest -v flaskr.tests.integration.test_database`
