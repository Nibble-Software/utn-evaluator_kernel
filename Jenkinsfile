pipeline{
    agent { docker { image 'python:3.8.10' } }

    stages{

        stage ("build"){
            steps{
                echo 'building enviroment'                
                sh 'pip install unittest'
            }
        }
        stage("test"){
            steps{
                echo 'testing file'
                sh 'cd CodeEvaluator'
                sh 'python -m unittest discover test'                
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