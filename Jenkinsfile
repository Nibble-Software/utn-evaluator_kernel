pipeline{
    agent {docker {image 'python:3.8.10-alpine'}}

    stages{

        stage ("build"){
            steps{
                echo 'building enviroment'                               
                
            }
        }
        stage("test"){
            steps{
                echo 'testing file'
                sh 'cd CodeEvaluator'
                sh 'python -m unittest discover'                
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