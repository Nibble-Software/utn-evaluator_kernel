pipeline{
    agent any

    stages{

        stage ("configuration"){
            steps{
                echo 'configuring enviroment'
                sh 'apt install python3'
                sh 'apt install pip3'
                sh 'pip3 install unittest'
            }
        }
        stage("test"){
            steps{
                echo 'testing file'
                sh 'cd CodeEvaluator'
                sh 'python3 -m unittest discover test'                
            }
        }
        stage("build"){
            steps{
                echo 'building project'
            }
        }
        stage("test-build"){
            steps{
                echo 'testing build'
            }
        }
        stage("publish"){
            steps{
                echo 'publishing in pip'
            }
        }
    }
}