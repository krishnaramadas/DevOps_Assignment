pipeline
{
    agent
    {
        docker
        {
            image 'python:3.8-slim-buster'
        }
    }

        stages {
        stage('build') {
            steps {
                sh 'calculator.py'
            }
        }
        stage('test') {
            steps {
                sh 'test_calculator.py'
            }
        }
    }
}
