pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "calculator-app"
        CONTAINER_NAME = "prem_con"  // Define the container name here
    }

    stages {
        stage('Checkout') {
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
        
        // stage('Run Calculator Operation') {
        //     steps {
        //         script {
        //             // Run the calculator operation (add 10 5) with the container name from environment
        //             sh "docker run --name ${CONTAINER_NAME} --rm ${DOCKER_IMAGE} python calculator.py add 10 5"
        //         }
        //     }
        // }

        // stage('Run Tests') {
        //     steps {
        //         script {
        //             // Run tests using pytest inside the Docker container
        //             sh "docker run --rm ${DOCKER_IMAGE} pytest --maxfail=1 --disable-warnings -q"
        //         }
        //     }
        // }

        // stage('Post-Build Cleanup') {
        //     steps {
        //         script {
        //             // Clean up Docker container and image after build

        //             // Remove the container (in case it was not removed by the --rm flag)
        //             sh "docker rm -f ${CONTAINER_NAME} || true"

        //             // Remove the Docker image
        //             sh "docker rmi ${DOCKER_IMAGE} || true"
        //         }
        //     }
        // }
    }
    
    post {
        success {
            echo 'Build and tests were successful!'
        }

        failure {
            echo 'Something went wrong during the build or tests!'
        }
    }
}
