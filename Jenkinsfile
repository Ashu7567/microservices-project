pipeline {
    agent any

    environment {
        IMAGE_NAME = "user-service-image"
        DOCKER_REPO = "ashu7567/user-service:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Debug - Show Directory') {
            steps {
                sh 'pwd'
                sh 'ls -l'
                sh 'ls -l user_service || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔨  Building Docker image...'
                sh 'docker build -t $IMAGE_NAME ./user-service'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪  Running Unit Tests...'
                sh 'docker run --rm $IMAGE_NAME pytest || true'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '📦  Pushing Docker Image to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag $IMAGE_NAME $DOCKER_REPO'
                    sh 'docker push $DOCKER_REPO'
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                echo '🚀  Deploying to remote server...'
                script {
                    sh """
                    ssh -o StrictHostKeyChecking=no root@142.93.66.255 << 'ENDSSH'
                    docker stop microservices-project_user-service_1  user-service || true
                    docker rm -f microservices-project_user-service_1  user-service || true
                    docker pull $DOCKER_REPO
                    docker run -d --name user-service -p 5001:5001 $DOCKER_REPO
                    ENDSSH
                                '''
                }
            }
        }
    }

    post {
        always {
            echo '✅  Build completed.'
        }
    }
}
