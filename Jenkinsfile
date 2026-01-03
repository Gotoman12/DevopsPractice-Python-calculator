pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                git url: "https://github.com/Gotoman12/DevopsPractice-Python-calculator.git",
                    branch: "Decsecops"
            }
        }

        stage("Setup Environment") {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage("Test") {
            steps {
                sh '''
                . venv/bin/activate
                python tests/test_app.py
                '''
            }
        }
    }
}
