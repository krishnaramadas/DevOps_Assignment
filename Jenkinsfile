pipeline {
    agent any

        stages {
        stage('build') {
            steps {
                bat 'python calculator.py'
            }
        }
        stage('test') {
            steps {
                bat 'python test_calculator.py'
            }
        }
    }
}
