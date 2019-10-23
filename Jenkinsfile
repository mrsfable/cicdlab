pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/build.sh"'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "test"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "deploy"'
      }
    }
  }
}