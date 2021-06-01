pipeline{
    agent {docker {image 'python:3.8.10-alpine'}}

    stages{

        stage ("build"){
            steps{
                echo 'building enviroment'
                sh 'yum install gcc g++ -y'
                                          
                
            }
        }
        stage("test"){
            steps{
                echo 'testing file'
                sh 'cd /var/jenkins_home/workspace/eline-evaluator-kernel_developer/CodeEvaluator && python -m unittest'           
                                
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