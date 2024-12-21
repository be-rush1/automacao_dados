pipeline {
  agent any
  parameters{
    string(name: "ANO_ARQUIVO", description: "Ano a partir que o arquivo vai ser baixado")
  }
  environment{
    NOME_ARQUIVO =  "${params.ANO_ARQUIVO}" 
  }
  stages {
    stage('Baixando dados a partir de ${params.ANO_ARQUIVO}') {
      steps {        
        
        sh """
        
        for x in {${params.ANO_ARQUIVO} ..2024} do
          wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/byYear/chirps-v2.0.${x}.monthly.nc
        done
        """

      }
    }
    stage('Corta os Dados') {
      steps {
         sh 'python3 corta_dados.py'
      }
    }
  }
}
