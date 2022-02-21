pipeline {
    agent any

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
