pipeline{
    agent any

   tools{
    python ""
   }
    stages{
        stage("GIT-CKECKOUT"){
            steps{
                git url:"https://github.com/Gotoman12/DevopsPractice-Python-calculator.git", branch: "Decsecops"
            }
        }
        stage("comiple"){
            steps{
                sh 'python3 pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage("test"){
            steps{
                sh 'python3 tests/test_app.py'
            }
        }
    }
}