pipeline{
    agent {docker {image 'chelo154/codeevaluator-kernel-test:0.0.1'}}

    stages{

        stage ("build"){
            steps{
                echo 'building enviroment'                                 
                
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