pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from the source repository
                checkout scm
            }
        }

        stage('Run Backend Server') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }

        stage('Run Frontend Server') {
            steps {
                bat 'start /min python web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                bat 'python backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                bat 'python frontend_testing.py'
            }
        }

        stage('Combined Testing') {
            steps {
                bat 'python combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }

    post {
        failure {
            // Send an email in case of a failure
            emailext (
                to: 'jankq79@gmail.com',
                subject: "Jenkins Build Failure: ${currentBuild.fullDisplayName}",
                body: """<p>There was a failure in the Jenkins build:</p>
                         <p><strong>${currentBuild.fullDisplayName}</strong></p>
                         <p>Check the build details at: ${env.BUILD_URL}</p>"""
            )
        }
    }
}