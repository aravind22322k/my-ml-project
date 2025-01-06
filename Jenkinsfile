pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aravind22322k/my-ml-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Preprocess Data') {
            steps {
                sh 'python3 scripts/preprocess.py'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 scripts/train.py'
            }
        }

        stage('Evaluate Model') {
            steps {
                sh 'python3 scripts/evaluate.py'
            }
        }

        stage('Deploy Model') {
            steps {
                sh 'python3 scripts/deploy.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
