pipeline {
  agent any
  parameters{
    string(name: "Ano-Arquivo", description: "Ano do arquivo a ser baixado")
  }
  stages {
    stage('Baixando dados de $params.Ano-Arquivo') {
      steps {
        
        sh 'echo ${params.Ano-Arquivo}'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 corta_dados.py'
      }
    }
  }
}
