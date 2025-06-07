pipeline {
    agent any 

    environment {
        MONGO_USER=credentials('mongo-user')
        MONGO_PASSWORD=credentials('mongo-passwod')
        MONGO_PORT=credentials('mongo-port')
    }

    stages {
        stage('Build') { 
            steps {
                echo 'Stage Build'
                sh 'docker-compose build'
                sh 'docker-compose up -d mongo app'

                post {
                    success {
                        echo 'Build was successful'
                    }
                    failure {
                        echo 'Build failed'
                    }
                }
            }
        }
        stage('Test') { 
            steps {
                echo 'Stage Test'
                sh 'docker-compose run --rm --service-ports test'

                post {
                    success {
                        echo 'Test was successful'
                    }
                    failure {
                        echo 'Test failed'
                    }
                }
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Stage Deploy'
                post {
                    success {
                        echo 'Deploy was successful'
                    }
                    failure {
                        echo 'Deploy failed'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline ended.'
        }
    }
}