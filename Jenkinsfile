pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh nginx-dev; /home/ec2-user/start.sh nginx-dev"'
          }
        }
        stage('') {
          steps {
            sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh backend"'
          }
        }
      }
    }
    stage('Test') {
      post {
        success {
          script {
            currentBuild.result = 'SUCCESS'
          }


        }

        failure {
          script {
            error "Failed, exiting now..."
          }


        }

      }
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/script/runTest.sh nginx-dev; /home/ec2-user/script/readResult.sh nginx-dev"'
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/script/compareResult.sh"'
      }
    }
    stage('Deploy') {
      parallel {
        stage('Deploy') {
          steps {
            sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh nginx-prod; /home/ec2-user/start.sh nginx-prod"'
          }
        }
        stage('') {
          steps {
            sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/start.sh backend"'
          }
        }
      }
    }
  }
}