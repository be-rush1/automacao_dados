pipeline {
  agent any
  parameters{
    string(name: "Ano-Arquivo", description: "Ano do arquivo a ser baixado")
  }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 corta_dados.py'
      }
    }
  }
}
