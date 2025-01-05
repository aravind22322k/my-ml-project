pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                    credentialsId: 'aravind22322k', 
                    url: 'https://github.com/aravind22322k/my-ml-project.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Preprocess Data') {
            steps {
                sh '''
                source venv/bin/activate
                python scripts/preprocess.py
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                source venv/bin/activate
                python scripts/train.py
                '''
            }
        }

        stage('Evaluate Model') {
            steps {
                sh '''
                source venv/bin/activate
                python scripts/evaluate.py
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                source venv/bin/activate
                python scripts/deploy.py
                '''
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
