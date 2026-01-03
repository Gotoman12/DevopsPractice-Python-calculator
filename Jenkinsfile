pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                git url: "https://github.com/Gotoman12/DevopsPractice-Python-calculator.git", branch: "Decsecops"
            }
        }

        stage("Install dependencies") {
            steps {
                sh '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage("Test") {
            steps {
                sh 'python tests/test_app.py'
            }
        }
    }
}
