pipeline {
    agent any
    stages {
        stage('Clone GITHUB Repository') {
            steps {
                checkout scm
            }
        }
        stage('Copy source code to Docker swarm') {
            steps {
                sh 'ansible-playbook playbook-to-copy-data-to-docker.yml --user=jenkins'
            }
        }

        stage('Build & Push the new Image to Dockerhub') {
            steps {
                sh 'ansible-playbook playbook-to-push.yml --user=jenkins'
            }
        }

        stage('Deploying new Service in Docker Swarm') {
            steps {
                sh 'ansible-playbook playbook-for-deployment.yml --user=jenkins'
            }
        }
    }
}
