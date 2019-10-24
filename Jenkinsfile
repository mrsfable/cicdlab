pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh; /home/ec2-user/start.sh"'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "test"'
        build 'mycicdlab'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "deploy"'
      }
    }
  }
}