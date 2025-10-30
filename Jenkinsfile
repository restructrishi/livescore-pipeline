pipeline {
    agent any

    environment {
        // !! CHANGE THIS to your Docker Hub username
        DOCKERHUB_USER = "rishingm" 
        DOCKERHUB_CREDS = "dockerhub-creds" 
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main', url: "${env.GIT_URL}"
            }
        }

        stage('2. SonarQube Analysis') {
            environment {
                SONAR_SCANNER_HOME = tool 'SonarScanner-5.0'
            }
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                    -Dsonar.projectKey=livescore-project \
                    -Dsonar.sources=frontend \
                    -Dsonar.inclusions=frontend/app.js \
                    -Dsonar.host.url=http://172.25.193.219:9000/ \
                    -Dsonar.login=admin \
                    -Dsonar.password=Admin@123
                    ''' 
                }
            }
        }
        
        stage('3. Quality Gate') {
            steps {
                echo "Checking SonarQube Quality Gate..."
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('4. Build Docker Images') {
            steps {
                echo "Building Docker images..."
                // We set the DOCKERHUB_USERNAME var for docker-compose
                sh "export DOCKERHUB_USERNAME=${DOCKERHUB_USER} && docker-compose build"
            }
        }

        stage('5. Push Docker Images') {
            steps {
                echo "Pushing images to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDS, passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKERHUB_USER}/livescore-backend:latest"
                    sh "docker push ${DOCKERHUB_USER}/livescore-frontend:latest"
                }
            }
        }

        stage('6. Deploy Locally') {
            steps {
                echo "Deploying application to local machine..."
                // Set the username var, pull new images, and restart
                sh """
                export DOCKERHUB_USERNAME=${DOCKERHUB_USER}
                docker-compose pull
                docker-compose down
                docker-compose up -d
                echo 'Deployment complete!'
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
            // Don't clean the workspace, so docker-compose.yml is available
            // cleanWs() 
            sh "docker logout"
        }
    }
}