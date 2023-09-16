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
                bat 'pip install -r requirements.txt'
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

        stage('Run Backend Tests') {
            steps {
                bat 'python backend_testing.py get 1'
            }
        }

        stage('Run Frontend Tests') {
            steps {
                bat 'python frontend_testing.py get 1'
            }
        }

        stage('Run Combined Tests') {
            steps {
                bat 'python combined_testing.py get 1'
            }
        }

        stage('Cleanup') {
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