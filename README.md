# Docker
Practices in docker

## Container commands
#### Create container
- Create a new cointainer by a image:

	`$ docker create image_reference`

	Examples:

	`$ docker create postgres`

	`$ docker create python:3.10`

- Create a new cointainer and assing a name:

	`$ docker create --name container_name image_reference`
 
	 Example:

	`$ docker create --name python3 python:3.10`

#### View containers
- Shows the container created and running

	`$ docker ps`

- Shows all container

	`$ docker ps -a`

#### Run container and stop
- **Run a container:**

	`$ docker start container_reference`

- **Stop a container:**

	`$ docker stop container_reference`

Examples:

`$ docker start python3`

`$ docker stop python3`

### View container logs
-  Latest logs:

	`$ docker logs container_reference`

- Real time logs: add --follow

	`$ docker logs --follow container_reference`

Examples:

`$ docker logs postgres`

`$ docker logs postgres`



#### Delete a container
`$ docker rm container_reference`

