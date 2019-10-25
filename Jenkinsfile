pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh nginx-dev; /home/ec2-user/start.sh nginx-dev"'
      }
    }
    stage('Test') {
      steps {
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/script/runTest.sh nginx-dev; /home/ec2-user/script/readResult.sh nginx-dev"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "deploy"'
        sh 'ssh -i "/DevOps.pem" -o StrictHostKeyChecking=no ec2-user@ec2-52-58-102-201.eu-central-1.compute.amazonaws.com "/home/ec2-user/build.sh nginx-prod; /home/ec2-user/start.sh nginx-prod"'
      }
    }
  }
}
