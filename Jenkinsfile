pipeline {
    agent any

    stages {
        stage("GIT-CHECKOUT") {
            steps {
                git url: "https://github.com/Gotoman12/DevopsPractice-Python-calculator.git", branch: "Decsecops"
            }
        }

        stage("Install pip & dependencies") {
            steps {
                 sh '''
                python3 --version
                python3 pip install --upgrade pip
                python3 pip install -r requirements.txt
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
