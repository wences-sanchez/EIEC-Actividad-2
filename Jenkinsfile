pipeline {
    agent {
        label ('docker || master')
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/wences-sanchez/EIEC-Actividad-3.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API tests') {
            steps {
                echo 'Testing the API'
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                echo 'End-to-end tests'
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {
            mail bcc: '', body: "<b>EIEC_Actividad-3</b><br>URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8',
                    from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR en el proyecto ${env.JOB_NAME}",
                    to: "wenceslaosanchezpino@gmail.com";
        }
    }
}