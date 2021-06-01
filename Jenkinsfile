pipeline{
    agent any

    stages{

        stage ("build"){
            steps{
                echo 'building enviroment'                               
                sh 'sudo apt install python3'
                sh 'sudo apt install pip3'
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
        stage("build-library"){
            steps{
                echo 'building project'
            }
        }
        stage("test-library"){
            steps{
                echo 'testing build'
            }
        }
        stage("publish-library"){
            steps{
                echo 'publishing in pip'
            }
        }
    }
}