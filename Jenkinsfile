pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub' // Replace with your Jenkins credentials ID
        DOCKER_IMAGE_NAME = 'premdatagrokr/calculator' // Format: <username>/<image_name>
        CONTAINER_NAME = 'add' // Define container name for reuse
    }

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the source code from the repository
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        
        stage('Run Calculator Operation') {
            steps {
                script {
                    // Run the calculator operation (add 10 5) with the container name from environment
                    sh "docker run --name ${CONTAINER_NAME} --rm ${DOCKER_IMAGE} python calculator.py add 10 5"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Run tests using pytest inside the Docker container
                    sh "docker run --rm ${DOCKER_IMAGE} pytest --maxfail=1 --disable-warnings -q"
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS_ID) {
                        // Push the Docker image
                        sh "docker push ${DOCKER_IMAGE_NAME}" // Use double quotes
                    }
                }
            }
        }

        stage('Post-Build Cleanup') {
            steps {
                script {
                    try {
                        // Stop and remove the container
                        bat "docker stop ${CONTAINER_NAME} || exit 0"
                        bat "docker rm ${CONTAINER_NAME} || exit 0"
                        
                        // Optionally remove the Docker image after the pipeline completes
                        bat "docker rmi ${DOCKER_IMAGE_NAME} || exit 0"
                    } catch (Exception e) {
                        error "Failed to clean up Docker resources: ${e.message}"
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Build, tests, and Docker push were successful!'
        }

        failure {
            echo 'Something went wrong during the build, tests, or Docker push!'
        }
    }
}
