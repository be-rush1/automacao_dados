pipeline {
  agent any
  parameters{
    string(name: "ANO_ARQUIVO", description: "Ano a partir que o arquivo vai ser baixado", defaultValue: "1981")
  }
  stages {
    stage("Baixando dados do CHIRPS") {
      steps {        
        sh '''
        echo "${params.ANO_ARQUIVO}"
        #for i in $(seq ${params.ANO_ARQUIVO} 2024); do
        #  wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/byYear/chirps-v2.0.${i}.monthly.nc
        #done 
           '''
      }
    }
    stage('Corta os Dados') {
      steps {
         sh 'python3 corta_dados.py'
      }
    }
  }
}
