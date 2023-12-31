pipeline {
    agent { docker { image 'python:3.8.10-alpine3.19' } }

    stages {
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python -m pytest'
            }
        }
        stage('Build') {
            steps {
                echo 'Building'
                sh 'pip install -r requirements.txt'
                sh 'python app.py'
            }
        }
        post {
            failure {
                mail(to: 'congthanhtr151@gmail.com', subject: 'The pipeline has been built failed')
            }
        }
    }
}