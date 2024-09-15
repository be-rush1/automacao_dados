pipeline {
  agent any
  parameters{
    string(name: "ANO_ARQUIVO", description: "Ano do arquivo a ser baixado")
  }
  environment{
    ANO_ARQUIVO =  "${params.ANO_ARQUIVO}"
  }
  stages {
    stage('Baixando dados de ${params.ANO_ARQUIVO}') {
      steps {
        
     //   sh """wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/byYear/chirps-v2.0.${params.ANO_ARQUIVO}.monthly.nc"""

        sh 'echo ${WORKSPACE}'

      }
    }
    stage('Corta os Dados') {
      steps {
         sh 'python3 corta_dados.py'
      }
    }
  }
}
