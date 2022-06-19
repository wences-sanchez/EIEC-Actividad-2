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
            junit 'results/*_result.xml', skipPublishingChecks: true
            cleanWs()
        }
        failure {
            echo "body: Project: ${env.JOB_NAME}\n Build Number: ${env.BUILD_NUMBER}\n URL de build: ${env.BUILD_URL}"
//            mail bcc: '', body: "<b>EIEC_Actividad-3</b><br>Project: ${env.JOB_NAME} <br> Build Number: ${env.BUILD_NUMBER}<br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', \
//                    from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR en el proyecto ${env.JOB_NAME}", \
//                    to: "wenceslaosanchezpino@gmail.com";
        }
    }
}