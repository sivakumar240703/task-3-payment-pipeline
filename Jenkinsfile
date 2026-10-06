pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = "localhost:5000/mycompany/payment"
        IMAGE_TAG = "${BUILD_NUMBER}"
        BRANCH_NAME = "main"
    }

    stages {

        stage('Build') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Test') {
            steps {
                bat "docker run --rm %IMAGE_NAME%:%IMAGE_TAG% pytest"
            }
        }

        stage('Tag') {
            steps {
                bat "docker tag %IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Push') {
            steps {
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy') {
            steps {
                bat """
                    docker stop payment
                    if %ERRORLEVEL% NEQ 0 echo No existing payment container found

                    docker rm payment
                    if %ERRORLEVEL% NEQ 0 echo No existing payment container to remove

                    docker run -d --name payment -p 8085:8080 -e APP_VERSION=%IMAGE_TAG% -e BUILD_NUMBER=%BUILD_NUMBER% -e GIT_COMMIT=%GIT_COMMIT% -e BRANCH_NAME=%BRANCH_NAME% -e DOCKER_IMAGE=%IMAGE_NAME%:%IMAGE_TAG% %IMAGE_NAME%:%IMAGE_TAG%
                """

                bat """
                    echo Application Version: %IMAGE_TAG%
                    echo Git Commit: %GIT_COMMIT%
                    echo Docker Image: %IMAGE_NAME%:%IMAGE_TAG%
                    echo Jenkins Build: %BUILD_NUMBER%
                    echo Branch: %BRANCH_NAME%
                """
            }
        }
    }
}
