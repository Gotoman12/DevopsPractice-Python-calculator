pipeline{
    agent any

    environment {
        IMAGE_NAME="arjunckm/python:${GIT_COMMIT}"
    }

    stages{
        stage("GIT-CKECKOUT"){
            steps{
                git url:"https://github.com/Gotoman12/DevopsPractice-Python-calculator.git", "main"
            }
        }
        stage("docker-build"){
            steps{
                sh 'docker build -t ${IMAGE_NAME} .'
            }

        }
        stage("docker-run"){
            steps{
                sh 'docker run -it -d --name python-calc -p 6001:5000 ${IMAGE_NAME}'
            }
        }
         stage("docker-login"){
            steps{
                script{
                    withCredentials([usernamePassword(credentialsId: 'docker_hubcred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Login to Docker Hub
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                 }
                }
            }
        }
        stage("docker-push"){
            steps{
                sh 'docker push ${IMAGE_NAME}'
            }
        }
    }
}