pipeline {
  agent any
  parameters{
    string(name: "Ano-Arquivo", description: "Ano do arquivo a ser baixado")
  }
  stages {
    stage('Baixando dados de $params.Ano-Arquivo') {
      steps {
        sh 'wget https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/byYear/chirps-v2.0.$params.Ano-Arquivo.monthly.nc'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 corta_dados.py'
      }
    }
  }
}
