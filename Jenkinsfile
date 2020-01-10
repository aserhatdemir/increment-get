pipeline {
  agent {
    docker {
      args '-p 5000:5000'
      image 'serhatdemir/increment-get:latest'
    }

  }
  stages {
    stage('s1') {
      steps {
        echo 'hello'
      }
    }
  }
}