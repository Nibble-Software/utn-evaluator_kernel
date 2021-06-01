pipeline{
    agent any

    stages{
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