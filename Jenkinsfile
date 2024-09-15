pipeline {
  agent any
  parameters{
    string(name: "ano_arquivo", description: "Ano do arquivo a ser baixado")
  }
  stages {
    stage('Baixando dados de ${params.Ano-Arquivo}') {
      steps {
        
     //   sh """wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/byYear/chirps-v2.0.${params.ano_arquivo}.monthly.nc"""

        sh 'echo ${WORKSPACE}'

      }
    }
    stage('Corta os Dados') {
      steps {
        sh 'echo olá'
     //   sh 'python3 corta_dados.py'
      }
    }
  }
}
