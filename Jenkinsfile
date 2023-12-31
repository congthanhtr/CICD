pipeline {
    agent {
        docker {image 'python:3.8.18-bullseye'}
    }

    stages {
        stage('Prepare') {
            steps {
                echo 'Preparing...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python -m pytest'
            }
        }
        stage('Build') {
            steps {
                echo 'Building'
                sh 'python app.py'
            }
        }
    }
}