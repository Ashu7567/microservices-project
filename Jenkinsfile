pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo '📥 Cloning repository from GitHub...'
                git 'https://github.com/Ashu7567/microservices-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                script {
                    sh 'docker build -t ashu7567/user-service:latest ./app'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                script {
                    sh 'docker run --rm ashu7567/user-service:latest python test_app.py'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo '📤 Pushing image to DockerHub...'
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push ashu7567/user-service:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                echo '🚀 Deploying to remote server...'
                script {
                    sh '''
                    ssh -o StrictHostKeyChecking=no root@142.93.66.255 << EOF
                    docker rm -f user-service || true
                    docker pull ashu7567/user-service:latest
                    docker run -d -p 5001:5001 --name user-service ashu7567/user-service:latest
                    EOF
                    '''
                }
            }
        }
    }
}
