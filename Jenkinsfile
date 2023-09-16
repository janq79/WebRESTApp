pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Delete workspace
                    deleteDir()
                }
            }
        }

        stage('Checkout') {
            steps {
                // This will automatically checkout your source code
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Backend Server') {
            steps {
                script {
                    bat 'start /min python rest_app.py'
                    sleep 10 // Wait for server to start up. Adjust time as necessary.
                }
            }
        }

        stage('Run Frontend Server') {
            steps {
                script {
                    bat 'start /min python web_app.py'
                    sleep 10 // Wait for server to start up. Adjust time as necessary.
                }
            }
        }

        stage('Run Backend Tests') {
            steps {
                bat 'python backend_testing.py'
            }
        }

        stage('Run Frontend Tests') {
            steps {
                bat 'python frontend_testing.py'
            }
        }

        stage('Run Combined Tests') {
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
        always {
            // This will always run, regardless of build status
            echo "Always block..."
        }
        success {
            // This will only run if the build was successful
            echo "Build was successful!"
        }
        failure {
            // This will only run if the build failed
            echo "Build failed!"
            mail(to: 'janq79@gmail.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something went wrong with ${env.BUILD_URL}")
        }
    }
}