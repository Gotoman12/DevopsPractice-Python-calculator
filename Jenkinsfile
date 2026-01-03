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
                python3 --version
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage("Test") {
            steps {
                sh 'python3 tests/test_app.py'
            }
        }
    }
}
