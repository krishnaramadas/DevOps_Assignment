pipeline {
    agent any

        stages {
        stage('build') {
            steps {
                sh 'python calculator.py'
            }
        }
        stage('test') {
            steps {
                sh 'python test_calculator.py'
            }
        }
    }
}
