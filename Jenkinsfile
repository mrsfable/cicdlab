pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh; /home/ec2-user/start.sh"'
      }
    }
    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'curl -H \'loaderio-auth: 9b7cedac3d569b020fefe4f94227490f\' https://api.loader.io/v2/tests/49b5c151dc02373dd4cf6e4a147ba991/run'
          }
        }
        stage('') {
          environment {
            Ci = 'true'
          }
          steps {
            sh './jenkins/scripts/test.sh '
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "deploy"'
      }
    }
  }
}