pipeline {
    agent any

    parameters {
        string(name: 'USER_ID', defaultValue: '1', description: 'User ID for tests')
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    deleteDir()
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run docker-compose up') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Backend Server') {
            steps {
                sh 'nohup python rest_app.py &'
            }
        }

        stage('Run Frontend Server') {
            steps {
                sh 'nohup python web_app.py &'
            }
        }

        stage('Run Backend Tests') {
            steps {
                sh "python backend_testing.py get ${params.USER_ID}"
            }
        }

        stage('Run Frontend Tests') {
            steps {
                sh "python frontend_testing.py test ${params.USER_ID}"
            }
        }

        stage('Run Combined Tests') {
            steps {
                sh "python combined_testing.py test ${params.USER_ID}"
            }
        }

        stage('Test Dockerized App') {
            steps {
                sh "python docker_backend_testing.py get ${params.USER_ID}"
            }
        }
    }

    post {
        always {
            sh 'python clean_environment.py'
            sh 'docker-compose down'
            sh 'docker rmi myapp:${BUILD_NUMBER}'
            echo "Always block executed..."
        }
        success {
            echo "Build was successful!"
        }
        failure {
            echo "Build failed!"
            mail(to: 'janq79@gmail.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something went wrong with ${env.BUILD_URL}")
        }
    }
}