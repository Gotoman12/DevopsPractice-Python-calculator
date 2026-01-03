pipeline{
    agent any

    stages{
        stage("GIT-CKECKOUT"){
            steps{
                git url:"https://github.com/Gotoman12/DevopsPractice-Python-calculator.git", branch: "Decsecops"
            }
        }
        stage("comiple"){
            steps{
                sh '''
                apt-get update && apt-get install -y python3 python3-pip
                pip3 install --no-cache-dir -r requirements.txt
                '''
            }
        }
        stage("test"){
            steps{
                sh 'python3 tests/test_app.py'
            }
        }
    }
}