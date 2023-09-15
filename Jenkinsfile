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

        stage('Build and Test') {
            steps {
                // Your build and test steps go here
                echo "Building and testing..."
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